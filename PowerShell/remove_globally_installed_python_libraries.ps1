$InstalledGlobalPythonPackages =  pip freeze
$InstalledGlobalPythonPackages

# for each package in the list, run "pip uninstall -y <package>"
# for example, if the list contains "numpy", run "pip uninstall -y numpy"
foreach ($package in $InstalledGlobalPythonPackages) {
    pip uninstall -y $package
}

echo "All packages uninstalled"
echo "Installed packages:"
pip freeze