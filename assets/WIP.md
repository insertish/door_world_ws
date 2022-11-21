### Work towards getting this to work with apptainer

Build a sandbox container:

```bash
mkdir -p ~/Applications/tiago-pal
apptainer build --sandbox ~/Applications/tiago-pal docker:palroboticssl/tiago_tutorials:melodic
```

Then drop into the container:

```bash
apptainer run --nvccli --writable ~/Applications/tiago-pal
```

Source tiago workspace:

```bash
cd /tiago_public_ws
source devel/setup.bash
```

Build this workspace with tiago workspace overlayed:

```bash
cd $HOME/Projects/ITR/door_world_ws
rm -r build devel
catkin_make
source devel/setup.bash
```
