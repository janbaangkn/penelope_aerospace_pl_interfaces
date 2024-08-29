from setuptools import find_packages, setup

package_name = "penelope_fokker_module"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        # ("lib/" + package_name, [package_name + "/example_action_client.py"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Eugenio Bernardi",
    maintainer_email="e.bernardi@tudelft.nl",
    description="Simple example of a ROS2 action server and client for the PeneloPe specific interfaces",
    license="BSD-3-Clause",
    entry_points={
        "console_scripts": [
            "action_server = penelope_fokker_module.fokker_action_server:main",
        ],
    },
)
