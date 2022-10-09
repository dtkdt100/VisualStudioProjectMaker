# VisualStudioProjectMaker
Creates for you empty solution with three different projects: tests (GTest), main, and your lib files. 

The main and tests projects are linked to the lib files.

## Usage

1. Clone the repo: `git clone https://github.com/dtkdt100/VisualStudioProjectMaker.git`
2. Open your cli (make sure you have python3)
3. Run the follwing command: `python3 .\repo_generator.py <destination_path> <new_project_name>`

note: there is third option: <old_project_path>, it will change the path of the BaseRepo to your project that you want to clone.
Actually It will just copy your solution and change it's name

4. Open .sln file in visual studio
5. Build the lib files. Right click on the first project under solution label -> build.
6. Right click on main prkect -> set as startup project.
7. Run

## Examples

`python3 .\repo_generator.py C:\temp NewTwoCarsCppRepo C:\Users\dolev\source\repos\two_cars_cpp`

`python3 .\repo_generator.py C:\temp NewBaseRepo`
