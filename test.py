import os

def generate_readme(project_name, description, technologies, installation_instructions, usage_instructions, license_info, location):
    # Create README content dynamically
    readme_content = f"# {project_name}\n\n"
    readme_content += f"## Description\n{description}\n\n"
    readme_content += f"## Technologies Used\n{', '.join(technologies)}\n\n"
    readme_content += f"## Installation Instructions\n{installation_instructions}\n\n"
    readme_content += f"## Usage Instructions\n{usage_instructions}\n\n"
    readme_content += f"## License\n{license_info}\n"
    
    # Ensure the location is valid
    if not os.path.exists(location):
        print("The specified location does not exist. Creating the directory...")
        os.makedirs(location)

    # Define the full path for the README file
    readme_path = os.path.join(location, "README.md")

    # Write content to README.md
    with open(readme_path, "w") as file:
        file.write(readme_content)
    
    print(f"README.md file has been generated successfully at {readme_path}.")

# Ask for dynamic input from the user
project_name = input("Enter the project name: ")
description = input("Enter the project description: ")
technologies = input("Enter the technologies used (comma separated): ").split(",")
installation_instructions = input("Enter the installation instructions: ")
usage_instructions = input("Enter the usage instructions: ")
license_info = input("Enter the license information (e.g., MIT License): ")

# Ask the user for the location to save the README file
location = input("Enter the location where you want to generate the README file: ")

# Generate the README file
generate_readme(project_name, description, technologies, installation_instructions, usage_instructions, license_info, location)