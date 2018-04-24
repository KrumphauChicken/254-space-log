Homework 3:
===========

This branch is a working copy Space Log from homework 2 set up to be installed on a Linux system. I've moved the main executable to bin/, and the supporting files to lib/.

Requirements summary:
------------------
1. Create a VirtualBox virtual machine using Vagrant.
	- Use the [bento/debian-9](https://app.vagrantup.com/bento/boxes/debian-9) box (or [bento/debian-9.4-i386](https://app.vagrantup.com/bento/boxes/debian-9.4-i386) if you can't virtualize 64-bit). 
1. *Provision* your virtual machine by writing an inline Bash script inside the Vagrant file that downloads the Space Log program from this branch and installs it.

Submit your completed Vagrantfile via Titanium before 2018-4-29 (Sunday) at midnight.

Detailed requirements and notes:
--------------------------------
- **"How do I use Vagrant?"**
	- Install Vagrant on your computer, not on the virtual machine that you use for class. Don't go nesting VMs. If you have a Mac, you'll issue your commands, like `vagrant up` from Terminal. If you're using Windows, use PowerShell.
	- Consult the documentation at [Vagrant's website](https://www.vagrantup.com/docs/). The pages you need to read for this homework are Commands, Vagrantfile, Boxes, and Provisioning.
	- The default Vagrantfile created when you `vagrant init` is very well commented, and contains examples.
- **"How do I download this specific branch?"**
	- `git clone --branch homework3`
	- This is the same as a regular `git clone` followed by `git checkout homework3`, except you don't have to `cd` in and out of the directory in your Bash script.
- **"How am I supposed to know which directory to install things in?"**
	- You can put the `spacelog` executable in `/usr/bin/` or `/usr/local/bin`.
	- To find out where the library files go, find where Python files are installed normally.
		- Example: install numpy with `apt install python3-numpy`, and using `dpkg-query` to list the files in the `python3-numpy` package.
		- Look at the import statements in `spacelog` for another clue.
- **"How can I test my homework?"**
	- The first step is to test that your Vagrantfile runs without errors, correctly fetches, starts, and provisions the box.
	- The second is to test `spacelog`. To grade every submission, I will `vagrant ssh` into your machine, and run `spacelog 254-space-log/elite.log -[something]` to test it, so make sure that works.
		- (That assumes your provisioning script keeps the cloned repo sitting in the home folder inside the VM, so please do so. Vagrant is about dispensable testing environments; there isn't a need to clean/organize your VM's home folder.)
