%global         debug_package %{nil}
%global         __strip /bin/true
%global		_basever 9.1.85
%define md5_cuda_x86_64		67a5c3933109507df6b68f80650b4b4a  

Name:           cuda
Version:        9.1.85.2
Release:        1%{?dist}
Summary:        Installer for the NVIDIA Compute Unified Device Architecture Toolkit
License:        NVIDIA License
URL:            https://developer.nvidia.com/cuda-zone
ExclusiveArch:  x86_64 %{ix86}

Source3:	cuda.sh
Source4:	cuda.conf

BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
# For execstack removal
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  execstack
BuildRequires:  perl(Getopt::Long)
%else
BuildRequires:  prelink
%endif
BuildRequires:	wget perl
BuildRequires:  chrpath


%description
This package will download and install the proprietary NVIDIA CUDA Toolkit.

CUDA is a parallel computing platform and programming model that enables
dramatic increases in computing performance by harnessing the power of the
graphics processing unit (GPU).


%prep
install -d %{_builddir}/%{name}-%{version}

%build
#nothing here

%install

# Install profile and ld.so.config files
install -Dm755 %{S:3} "%{buildroot}/etc/profile.d/cuda.sh"
install -Dm644 %{S:4} "%{buildroot}/etc/ld.so.conf.d/cuda.conf"

install -d %{buildroot}/opt/cuda/bin/crt/ %{buildroot}/opt/cuda/bin/nvdisasm %{buildroot}/usr/share/applications/
install -d %{buildroot}/etc/ld.so.conf.d

mkdir -p "%{buildroot}/usr/share/licenses/%{name}"
ln -sf /opt/cuda/doc/pdf/EULA.pdf "%{buildroot}/usr/share/licenses/%{name}/EULA.pdf"

touch %{buildroot}/opt/cuda/bin/bin2c
chmod 755 %{buildroot}/opt/cuda/bin/bin2c
touch %{buildroot}/opt/cuda/bin/computeprof
chmod 755 %{buildroot}/opt/cuda/bin/computeprof
touch %{buildroot}/opt/cuda/bin/crt/link.stub
chmod 755 %{buildroot}/opt/cuda/bin/crt/link.stub
touch %{buildroot}/opt/cuda/bin/crt/prelink.stub
chmod 755 %{buildroot}/opt/cuda/bin/crt/prelink.stub
touch %{buildroot}/opt/cuda/bin/cuda-gdb
chmod 755 %{buildroot}/opt/cuda/bin/cuda-gdb
touch %{buildroot}/opt/cuda/bin/cuda-gdbserver
chmod 755 %{buildroot}/opt/cuda/bin/cuda-gdbserver
touch %{buildroot}/opt/cuda/bin/cuda-install-samples-9.1.sh
chmod 755 %{buildroot}/opt/cuda/bin/cuda-install-samples-9.1.sh
touch %{buildroot}/opt/cuda/bin/cuda-memcheck
chmod 755 %{buildroot}/opt/cuda/bin/cuda-memcheck
touch %{buildroot}/opt/cuda/bin/cudafe
chmod 755 %{buildroot}/opt/cuda/bin/cudafe
touch %{buildroot}/opt/cuda/bin/cudafe++
chmod 755 %{buildroot}/opt/cuda/bin/cudafe++
touch %{buildroot}/opt/cuda/bin/cuobjdump
chmod 755 %{buildroot}/opt/cuda/bin/cuobjdump
touch %{buildroot}/opt/cuda/bin/fatbinary
chmod 755 %{buildroot}/opt/cuda/bin/fatbinary
touch %{buildroot}/opt/cuda/bin/gpu-library-advisor
chmod 755 %{buildroot}/opt/cuda/bin/gpu-library-advisor
touch %{buildroot}/opt/cuda/bin/nsight
chmod 755 %{buildroot}/opt/cuda/bin/nsight
touch %{buildroot}/opt/cuda/bin/nsight_ee_plugins_manage.sh
chmod 755 %{buildroot}/opt/cuda/bin/nsight_ee_plugins_manage.sh
touch %{buildroot}/opt/cuda/bin/nvcc
chmod 755 %{buildroot}/opt/cuda/bin/nvcc
touch %{buildroot}/opt/cuda/bin/nvcc.profile
chmod 755 %{buildroot}/opt/cuda/bin/nvdisasm
touch %{buildroot}/opt/cuda/bin/nvdisasm
chmod 755 %{buildroot}/opt/cuda/bin/nvdisasm
touch %{buildroot}/opt/cuda/bin/nvlink
chmod 755 %{buildroot}/opt/cuda/bin/nvlink
touch %{buildroot}/opt/cuda/bin/nvprof
chmod 755 %{buildroot}/opt/cuda/bin/nvprof
touch %{buildroot}/opt/cuda/bin/nvprune
chmod 755 %{buildroot}/opt/cuda/bin/nvprune
touch %{buildroot}/opt/cuda/bin/nvvp
chmod 755 %{buildroot}/opt/cuda/bin/nvvp
touch %{buildroot}/opt/cuda/bin/ptxas
chmod 755 %{buildroot}/opt/cuda/bin/ptxas
touch %{buildroot}/opt/cuda/bin/uninstall_cuda_toolkit_9.1.pl
chmod 755 %{buildroot}/opt/cuda/bin/uninstall_cuda_toolkit_9.1.pl
touch %{buildroot}/%{_datadir}/applications/nsight.desktop
chmod 755 %{buildroot}/%{_datadir}/applications/nsight.desktop
touch  %{buildroot}/%{_datadir}/applications/nvvp.desktop
chmod 755 %{buildroot}/%{_datadir}/applications/nvvp.desktop

%pre

rm -rf /usr/src/cuda/
rm -rf /opt/cuda/

mkdir -p /usr/src/%{name}
echo 'Downloading CUDA, please wait...'
pushd /usr/src >/dev/null 2>&1
wget -c https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda_%{_basever}_387.26_linux
wget -c https://developer.nvidia.com/compute/cuda/9.1/Prod/patches/1/cuda_9.1.85.1_linux
wget -c https://developer.nvidia.com/compute/cuda/9.1/Prod/patches/2/cuda_9.1.85.2_linux

if [ -f /usr/src/cuda_%{_basever}_387.26_linux ] ; then
    #
    # Check the package
    #
if [ "$( md5sum cuda_%{_basever}_387.26_linux | awk '{print $1}' )" != %{md5_cuda_x86_64} ]; then
echo 'md5 sums mismatch'
rm -f cuda_%{_basever}_387.26_linux
else
echo 'checksums OK'
fi
fi
#
if [ ! -f /usr/src/cuda_%{_basever}_387.26_linux ]; then
    #
    # Get the package
    #
    echo 'Downloading CUDA, please wait...'
    wget -c https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda_%{_basever}_387.26_linux
    #
    # Check the package
    #
if [ "$( md5sum cuda_%{_basever}_387.26_linux | awk '{print $1}' )" != %{md5_cuda_x86_64} ]; then
echo 'md5 sums mismatch'
rm -f cuda_%{_basever}_387.26_linux
else
echo 'checksums OK'
fi
fi
#

sh cuda_%{_basever}_387.26_linux --extract=/usr/src/%{name}/ --nox11  

# path hacks
pushd /usr/src/%{name} >/dev/null 2>&1
./cuda-*.run -prefix=/opt/%{name}/ --noexec --keep --nox11 
./cuda-samples*.run -prefix=/opt/%{name}/ --noexec --keep --nox11 

  sed -e 's|can_add_for_all_users;|1;|g' \
      -e 's|=\\"$prefix\\\"|=/opt/cuda|g' -e 's|Terminal=No|Terminal=false|g' -e 's|ParallelComputing|ParallelComputing;|g' \
      -i pkg/install-linux.pl

  # set right path in Samples Makefiles
  sed 's|\$cudaprefix\\|\\/opt\\/cuda\\|g' -i pkg/install-sdk-linux.pl

  # use python2
  find pkg -name '*.py' | xargs sed -i -e 's|env python|env python2|g' -e 's|bin/python|bin/python2|g'

mkdir -p /opt/cuda/samples

  pushd pkg
  export PERL5LIB=.
  perl install-linux.pl -prefix="/opt/cuda" -noprompt
  perl install-sdk-linux.pl -cudaprefix="/opt/cuda" -prefix="/opt/cuda/samples" -noprompt
  sh /usr/src/cuda_9.1.85.1_linux --silent --accept-eula --installdir="/opt/cuda" --nox11
  sh /usr/src/cuda_9.1.85.2_linux --silent --accept-eula --installdir="/opt/cuda" --nox11

  # Hack we need because of glibc 2.26
  # without which we couldn't compile anything at all.
  # Super dirty hack. I really hope it doesn't break other stuff!
  # Hopefully we can remove this for later version of cuda.
  sed -i "1 i#define _BITS_FLOATN_H" "/opt/cuda/include/host_defines.h"

  # Needs gcc6, coming soon
  #ln -s /usr/bin/gcc-6 "/opt/cuda/bin/gcc"
  #ln -s /usr/bin/g++-6 "/opt/cuda/bin/g++"


  # Remove redundant man and samples
  rm -fr "/opt/cuda/doc/man"
  rm -fr "/opt/cuda/cuda-samples"
  rm -fr "/usr/share/man/man3/deprecated.3"*

  # Remove included copy of java and link to system java
  rm -fr  "/opt/cuda/jre"
  sed 's|../jre/bin/java|/usr/bin/java|g' \
    -i "/opt/cuda/libnsight/nsight.ini" \
    -i "/opt/cuda/libnvvp/nvvp.ini"

  # Cleaning the house
  rm -rf /usr/src/cuda

#
/sbin/ldconfig
#

%postun 
perl /opt/cuda/bin/uninstall_cuda_toolkit_9.1.pl
perl /opt/cuda/samples/uninstall_cuda_samples_9.1.pl
#
if [ "$1" == "0" ] ; then
#
[ -d /opt/cuda ] && rm -rf /opt/cuda
#
fi
#
/sbin/ldconfig
#

%files
%license EULA.pdf
%ghost /opt/cuda/
%ghost %{_mandir}/*/*.gz
%{_sysconfdir}/ld.so.conf.d/cuda.conf
%{_sysconfdir}/profile.d/cuda.sh
%ghost %{_datadir}/applications/nsight.desktop
%ghost %{_datadir}/applications/nvvp.desktop

%changelog

* Mon Apr 16 2018 - David Vasquez <davidva AT tutanota DOT com>  9.1.85.2-1
- Initial release
