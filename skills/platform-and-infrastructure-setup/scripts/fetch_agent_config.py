import argparse
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

# Registry URL
REGISTRY_URL = "https://npm.mspbots.ai/"
# Credentials
AUTH_EMAIL = "admin@mspbots.ai"
AUTH_TOKEN = "YWRtaW46TW9UUkxqdSFhQzQ/"

def install_agent(agent_id):
    # Output is always current working directory
    output_dir = Path.cwd()
    print(f"Target directory for installation: {output_dir}")

    package_name = f"@agent/{agent_id}"
    print(f"Attempting to download package: {package_name} from {REGISTRY_URL}")

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        try:
            # Check if npm is installed
            subprocess.run(["npm", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=os.name == 'nt')
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: 'npm' command not found. Please ensure Node.js/npm is installed and in your PATH.")
            sys.exit(1)

        try:
            # Generate .npmrc with authentication
            npmrc_path = temp_path / ".npmrc"
            
            # Parse registry URL for config key (remove protocol)
            # e.g., https://npm.mspbots.ai/ -> //npm.mspbots.ai/
            config_key_url = REGISTRY_URL.split("://")[1]
            if not config_key_url.endswith("/"):
                config_key_url += "/"
            
            with open(npmrc_path, "w") as f:
                f.write(f"registry={REGISTRY_URL}\n")
                f.write(f"//{config_key_url}:_auth={AUTH_TOKEN}\n")
                f.write(f"//{config_key_url}:email={AUTH_EMAIL}\n")
                f.write(f"//{config_key_url}:always-auth=true\n")
            
            # Download the package using npm pack
            cmd = [
                "npm", "pack", package_name,
                "--userconfig", str(npmrc_path),
                "--registry", REGISTRY_URL
            ]
            
            # Run npm pack in the temp directory so the .tgz lands there
            is_windows = os.name == 'nt'
            # We don't need to pass env if we use userconfig, but let's be safe and pass current env
            result = subprocess.run(cmd, cwd=temp_path, check=True, capture_output=True, text=True, shell=is_windows)
            
            # Find the .tgz file
            # npm pack output usually is the filename, but might have other output
            tgz_files = list(temp_path.glob("*.tgz"))
            if not tgz_files:
                print(f"Error: npm pack succeeded but no .tgz file found in {temp_path}")
                print("npm output:", result.stdout)
                sys.exit(1)
            
            tgz_file = tgz_files[0]
            print(f"Downloaded: {tgz_file.name}")

            # Extract the tarball
            extract_dir = temp_path / "extracted"
            extract_dir.mkdir()
            
            with tarfile.open(tgz_file, "r:gz") as tar:
                def is_within_directory(directory, target):
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                    tar.extractall(path, members, numeric_owner=numeric_owner) 
                
                safe_extract(tar, path=extract_dir)

            # npm packages usually contain a 'package' directory at root
            content_source = extract_dir / "package"
            if not content_source.exists():
                # If for some reason it's different, use the extracted root
                content_source = extract_dir

            print(f"Installing agent files to {output_dir}...")
            
            # Copy all files from content_source to output_dir
            # dirs_exist_ok=True allows overwriting/merging into current directory
            shutil.copytree(content_source, output_dir, dirs_exist_ok=True)
            print(f"Successfully installed agent files to {output_dir}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error running npm pack: {e.stderr}")
            if "404" in e.stderr:
                 print(f"Package {package_name} not found in registry.")
            elif "401" in e.stderr or "403" in e.stderr:
                 print(f"Authentication failed for {REGISTRY_URL}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Install MSPBots agent from npm registry.")
    parser.add_argument("agent_id", help="The ID of the agent to install.")
    
    args = parser.parse_args()
    install_agent(args.agent_id)

if __name__ == "__main__":
    main()
