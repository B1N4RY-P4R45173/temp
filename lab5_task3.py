import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

# Create an empty disk image
run_command("dd if=/dev/zero of=disk.img bs=1M count=100")

# Format the disk image with ext4 filesystem
run_command("mkfs.ext4 disk.img")

# Create a mount point
mount_point = "/mnt/new_folder_name"
if not os.path.exists(mount_point):
    os.makedirs(mount_point)

# Mount the disk image
run_command(f"sudo mount -o loop disk.img {mount_point}")

# Copy an example image file to the mounted partition
image_file_path = "/path/to/your/image/file.jpg"
run_command(f"sudo cp {image_file_path} {mount_point}")

# Unmount the disk image
run_command(f"sudo umount {mount_point}")

# Mount the disk image again
run_command(f"sudo mount -o loop disk.img {mount_point}")

# Use dd to copy the image file from the mounted partition
run_command(f"dd if={mount_point}/file.jpg of=output.jpg bs=1M")

# Unmount the disk image
run_command(f"sudo umount {mount_point}")
