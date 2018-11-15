# tips thanks 
# negativo17
# Arch Linux

%global         debug_package %{nil}
%global		_missing_build_ids_terminate_build 0
%define 	fancy_debuginfo 0
%global         __strip /bin/true
#
%global		_basever 10.0.130
%global         _driverver 410.48
%global		cudadir /opt/cuda
%global		cuda_bin /opt/cuda/bin
%global		cuda_lib /opt/cuda/%{_lib}
%global		cuda_include /opt/cuda/include
%global		cuda_data /opt/cuda/share
%global		cuda_doc /opt/cuda/doc

%bcond_without normalsource

Name:           cuda
Version:        10.0.130
Release:        1%{?dist}
Summary:        Installer for the NVIDIA Compute Unified Device Architecture Toolkit
License:        NVIDIA License
URL:            https://developer.nvidia.com/cuda-zone
ExclusiveArch:  x86_64 %{ix86}

Source0:	https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_%{_basever}_%{_driverver}_linux
Source3:	cuda.sh
Source4:	cuda.conf
Source12:       nsight.desktop
Source13:       nsight.appdata.xml
Source14: 	nvvp.desktop
Source15:	nvvp.appdata.xml
# pkg-config files 
Source16:	cublas.pc
Source17:	cuda.pc
Source18:	cudart.pc
Source19:	cufft.pc
Source20:	curand.pc
Source21:	cusolver.pc
Source22:	cusparse.pc
Source23:	npp.pc
Source24:	nvgraph.pc
Source25:	nvml.pc
Source26:	nvrtc.pc
Source27:	nvToolsExt.pc

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
Recommends:	gcc7

%description
This package will download and install the proprietary NVIDIA CUDA Toolkit.

CUDA is a parallel computing platform and programming model that enables
dramatic increases in computing performance by harnessing the power of the
graphics processing unit (GPU).

%package cli-tools
Summary:        Compute Unified Device Architecture command-line tools
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       expat >= 1.95

%description cli-tools
Contains the command line tools to debug and profile CUDA applications.

%package libs
Summary:        Compute Unified Device Architecture native run-time library
Requires(post): ldconfig
# Explicitly declare the dependency or libcuda.so.1()(64bit) will pull in xorg-x11-drv-cuda-libs
Requires:       nvidia-driver-cuda-libs

%description libs
Contains the CUDA run-time library required to run CUDA application natively.

%package extra-libs
Summary:        All runtime NVIDIA CUDA libraries
Requires(post): ldconfig
Requires:       %{name}-cublas = %{version}-%{release}
Requires:       %{name}-cudart = %{version}-%{release}
Requires:       %{name}-cufft = %{version}-%{release}
Requires:       %{name}-cupti = %{version}-%{release}
Requires:       %{name}-curand = %{version}-%{release}
Requires:       %{name}-cusolver = %{version}-%{release}
Requires:       %{name}-cusparse = %{version}-%{release}
Requires:       %{name}-npp = %{version}-%{release}
Requires:       %{name}-nvgraph = %{version}-%{release}
Requires:       %{name}-nvrtc = %{version}-%{release}
Requires:       %{name}-nvtx = %{version}-%{release}

%description extra-libs
Metapackage that installs all runtime NVIDIA CUDA libraries.

%package cublas
Summary:        NVIDIA CUDA Basic Linear Algebra Subroutines (cuBLAS) libraries
Requires(post): ldconfig

%description cublas
The NVIDIA CUDA Basic Linear Algebra Subroutines (cuBLAS) library is a
GPU-accelerated version of the complete standard BLAS library that delivers 6x
to 17x faster performance than the latest MKL BLAS.

%package cublas-devel
Summary:        Development files for NVIDIA CUDA Basic Linear Algebra Subroutines (cuBLAS)
Requires:       %{name}-cublas = %{version}-%{release}

%description cublas-devel
This package provides development files for the NVIDIA CUDA Basic Linear
Algebra Subroutines (cuBLAS) libraries.

%package cudart
Summary:        NVIDIA CUDA Runtime API library
Requires(post): ldconfig

%description cudart
The runtime API eases device code management by providing implicit initialization,
context management, and module management. This leads to simpler code, but it
also lacks the level of control that the driver API has.

In comparison, the driver API offers more fine-grained control, especially over
contexts and module loading. Kernel launches are much more complex to implement,
as the execution configuration and kernel parameters must be specified with
explicit function calls. However, unlike the runtime, where all the kernels are
automatically loaded during initialization and stay loaded for as long as the
program runs, with the driver API it is possible to only keep the modules that
are currently needed loaded, or even dynamically reload modules. The driver API
is also language-independent as it only deals with cubin objects.

%package cudart-devel
Summary:        Development files for NVIDIA CUDA Runtime API library
Requires:       %{name}-cudart = %{version}-%{release}

%description cudart-devel
This package provides development files for the NVIDIA CUDA Runtime API library

%package cufft
Summary:        NVIDIA CUDA Fast Fourier Transform library (cuFFT) libraries
Requires(post): ldconfig

%description cufft
The NVIDIA CUDA Fast Fourier Transform libraries (cuFFT) provide a simple
interface for computing FFTs up to 10x faster.  By using hundreds of processor
cores inside NVIDIA GPUs, cuFFT delivers the floating‐point performance of a
GPU without having to develop your own custom GPU FFT implementation.

%package cufft-devel
Summary:        Development files for NVIDIA CUDA Fast Fourier Transform library (cuFFT)
Requires:       %{name}-cufft = %{version}-%{release}

%description cufft-devel
This package provides development files for the NVIDIA CUDA Fast Fourier
Transform library (cuFFT) libraries.

%package cupti
Summary:        NVIDIA CUDA Profiling Tools Interface (CUPTI) library
Requires(post): ldconfig

%description cupti
The NVIDIA CUDA Profiling Tools Interface (CUPTI) provides performance analysis
tools with detailed information about how applications are using the GPUs in a
system.

%package cupti-devel
Summary:        Development files for NVIDIA CUDA Profiling Tools Interface (CUPTI) library
Requires:       %{name}-cupti = %{version}-%{release}

%description cupti-devel
This package provides development files for the NVIDIA CUDA Profiling Tools
Interface (CUPTI) library.

%package curand
Summary:        NVIDIA CUDA Random Number Generation library (cuRAND)
Requires(post): ldconfig

%description curand
The NVIDIA CUDA Random Number Generation library (cuRAND) delivers high
performance GPU-accelerated random number generation (RNG). The cuRAND library
delivers high quality random numbers 8x faster using hundreds of processor
cores available in NVIDIA GPUs.

%package curand-devel
Summary:        Development files for NVIDIA CUDA Random Number Generation library (cuRAND)
Requires:       %{name}-curand = %{version}-%{release}

%description curand-devel
This package provides development files for the NVIDIA CUDA Random Number
Generation library (cuRAND).

%package cusolver
Summary:        NVIDIA cuSOLVER library
Requires(post): ldconfig
Requires:       libgomp

%description cusolver
The NVIDIA cuSOLVER library provides a collection of dense and sparse direct
solvers which deliver significant acceleration for Computer Vision, CFD,
Computational Chemistry, and Linear Optimization applications.

%package cusolver-devel
Summary:        Development files for NVIDIA cuSOLVER library
Requires:       %{name}-cusolver = %{version}-%{release}

%description cusolver-devel
This package provides development files for the NVIDIA cuSOLVER library.

%package cusparse
Summary:        NVIDIA CUDA Sparse Matrix library (cuSPARSE) library
Requires(post): ldconfig

%description cusparse
The NVIDIA CUDA Sparse Matrix library (cuSPARSE) provides a collection of basic
linear algebra subroutines used for sparse matrices that delivers up to 8x
faster performance than the latest MKL. The cuSPARSE library is designed to be
called from C or C++, and the latest release includes a sparse triangular
solver.

%package cusparse-devel
Summary:        Development files for NVIDIA CUDA Sparse Matrix library (cuSPARSE) library
Requires:       %{name}-cusparse = %{version}-%{release}

%description cusparse-devel
This package provides development files for the NVIDIA CUDA Sparse Matrix
library (cuSPARSE) library.

%package npp
Summary:        NVIDIA Performance Primitives libraries
Requires(post): ldconfig

%description npp
The NVIDIA Performance Primitives library (NPP) is a collection of
GPU-accelerated image, video, and signal processing functions that deliver 5x
to 10x faster performance than comparable CPU-only implementations. Using NPP,
developers can take advantage of over 1900 image processing and approx 600
signal processing primitives to achieve significant improvements in application
performance in a matter of hours.

%package npp-devel
Summary:        Development files for NVIDIA Performance Primitives
Requires:       %{name}-npp = %{version}-%{release}

%description npp-devel
This package provides development files for the NVIDIA Performance Primitives
libraries.

%package nvgraph
Summary:        NVIDIA Graph Analytics library (nvGRAPH)
Requires(post): ldconfig

%description nvgraph
The NVIDIA Graph Analytics library (nvGRAPH) comprises of parallel algorithms
for high performance analytics on graphs with up to 2 billion edges. nvGRAPH
makes it possible to build interactive and high throughput graph analytics
applications.

%package nvgraph-devel
Summary:        Development files for NVIDIA Graph Analytics library (nvGRAPH)
Requires:       %{name}-nvgraph = %{version}-%{release}

%description nvgraph-devel
This package provides development files for the NVIDIA Graph Analytics library
(nvGRAPH).

%package nvml-devel
Summary:        Development files for NVIDIA Management library (nvML)
# Unversioned as it is provided by the driver's NVML library
Requires:       %{name}-nvml

%description nvml-devel
This package provides development files for the NVIDIA Management library
(nvML).

%package nvrtc
Summary:        NVRTC runtime compilation library
Requires(post): ldconfig

%description nvrtc
NVRTC is a runtime compilation library for CUDA C++. It accepts CUDA C++ source
code in character string form and creates handles that can be used to obtain
the PTX. The PTX string generated by NVRTC can be loaded by cuModuleLoadData and
cuModuleLoadDataEx, and linked with other modules by cuLinkAddData of the CUDA
Driver API. This facility can often provide optimizations and performance not
possible in a purely offline static compilation.

%package nvrtc-devel
Summary:        Development files for the NVRTC runtime compilation library
Requires:       %{name}-nvrtc = %{version}-%{release}

%description nvrtc-devel
This package provides development files for the NVRTC runtime compilation
library.

%package nvtx
Summary:        NVIDIA Tools Extension
Requires(post): ldconfig

%description nvtx
A C-based API for annotating events, code ranges, and resources in your
applications. Applications which integrate NVTX can use the Visual Profiler to
capture and visualize these events and ranges.

%package nvtx-devel
Summary:        Development files for NVIDIA Tools Extension
Requires:       %{name}-nvtx = %{version}-%{release}

%description nvtx-devel
This package provides development files for the NVIDIA Tools Extension.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-cupti-devel = %{version}-%{release}
Requires:       %{name}-cublas-devel = %{version}-%{release}
Requires:       %{name}-cudart-devel = %{version}-%{release}
Requires:       %{name}-cufft-devel = %{version}-%{release}
Requires:       %{name}-cupti-devel = %{version}-%{release}
Requires:       %{name}-curand-devel = %{version}-%{release}
Requires:       %{name}-cusolver-devel = %{version}-%{release}
Requires:       %{name}-cusparse-devel = %{version}-%{release}
Requires:       %{name}-npp-devel = %{version}-%{release}
Requires:       %{name}-nvgraph-devel = %{version}-%{release}
Requires:       %{name}-nvml-devel = %{version}-%{release}
Requires:       %{name}-nvrtc-devel = %{version}-%{release}
Requires:       %{name}-nvtx-devel = %{version}-%{release}
Requires:	%{name}-nsight-compute = %{version}-%{release}
Provides:       %{name}-static = %{version}

%description devel
This package provides the development files of the %{name} package.

%package docs
Summary:        Compute Unified Device Architecture toolkit documentation
BuildArch:      noarch

%description docs
Contains all guides and library documentation for CUDA.

%package samples
Summary:        Compute Unified Device Architecture toolkit samples
Obsoletes:      %{name}-samples < %{version}
Provides:       %{name}-samples = %{version}
Requires:       cuda-devel = %{version}
%if 0%{?fedora} >= 28
Requires:       cuda-gcc-c++
%else
Requires:       gcc
%endif
Requires:       freeglut-devel
Requires:       make
Requires:       mesa-libGLU-devel
Requires:       libX11-devel
Requires:       libXmu-devel
Requires:       libXi-devel

%description samples
Contains an extensive set of example CUDA programs.

%package nsight
Summary:        NVIDIA Nsight Eclipse Edition
Requires:       %{name} = %{version}-%{release}

%description nsight
NVIDIA Nsight Eclipse Edition is a full-featured IDE powered by the Eclipse
platform that provides an all-in-one integrated environment to edit, build,
debug and profile CUDA-C applications. Nsight Eclipse Edition supports a rich
set of commercial and free plugins.

%package nvvp
Summary:        NVIDIA Visual Profiler
Requires:       %{name} = %{version}-%{release}

%description nvvp
The NVIDIA Visual Profiler is a cross-platform performance profiling tool that
delivers developers vital feedback for optimizing CUDA C/C++ applications.


%package nsight-compute
Summary:        NVIDIA Nsight Compute
Requires:       %{name} = %{version}-%{release}

%description nsight-compute
NVIDIA Nsight Compute is an interactive kernel profiler for CUDA applications. 
It provides detailed performance metrics and API debugging via a user interface 
and command line tool. In addition, its baseline feature allows users to compare 
results within the tool. Nsight Compute provides a customizable and data-driven 
user interface and metric collection and can be extended with analysis scripts 
for post-processing results.



%prep

install -d %{name}-%{version} 

%if !%{with normalsource}
wget -c https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_%{_basever}_%{_driverver}_linux
sh cuda_%{_basever}_387.26_linux --extract=$PWD/%{name}-%{name}/ --nox11
%else
sh %{S:0} --extract=$PWD/%{name}-%{version}/ --nox11
%endif

%autosetup -T -D -n %{name}-%{version}

# RPMlint issues
find . -name "*.h" -exec chmod 644 {} \;
find . -name "*.hpp" -exec chmod 644 {} \;
find . -name "*.bat" -delete
find . -size 0 -delete

%build
# nothing

%install

# path hacks
install -d %{buildroot}/opt/%{name}
./cuda-*.run -prefix=%{buildroot}/opt/%{name}/ --noexec --keep --nox11 
./cuda-samples*.run -prefix=%{buildroot}/opt/%{name}/ --noexec --keep --nox11 

sed -e "s|/usr/share|$PWD/../pkg/%{name}/usr/share|g" \
      -e 's|can_add_for_all_users;|1;|g' \
      -e 's|=\\"$prefix\\\"|=/opt/cuda|g' -e 's|Terminal=No|Terminal=false|g' -e 's|ParallelComputing|ParallelComputing;|g' \
      -i pkg/install-linux.pl

  # set right path in Samples Makefiles
  sed 's|\$cudaprefix\\|\\/opt\\/cuda\\|g' -i pkg/install-sdk-linux.pl

  # use python2
  find pkg -name '*.py' | xargs sed -i -e 's|env python|env python2|g' -e 's|bin/python|bin/python2|g'

  # Samples
  install -d %{buildroot}/opt/cuda/samples

  pushd pkg
  export PERL5LIB=.
  perl install-linux.pl -prefix="%{buildroot}/opt/cuda" -noprompt
  perl install-sdk-linux.pl -cudaprefix="%{buildroot}/opt/cuda" -prefix="%{buildroot}/opt/cuda/samples" -noprompt

# Install profile and ld.so.config files
install -Dm755 %{S:3} "%{buildroot}/etc/profile.d/cuda.sh"
install -Dm644 %{S:4} "%{buildroot}/etc/ld.so.conf.d/cuda.conf"

# Convert icons for appstream
convert libnsight/icon.xpm nsight.png
convert libnvvp/icon.xpm nvvp.png

# Install icons for desktop file
install -d %{buildroot}/%{_datadir}/pixmaps 
install -m 644 $PWD/nsight.png %{buildroot}/%{_datadir}/pixmaps/nsight.png
install -m 644 $PWD/nvvp.png %{buildroot}/%{_datadir}/pixmaps/nvvp.png

desktop-file-install --dir %{buildroot}/%{_datadir}/applications/ %{SOURCE12} %{SOURCE14}

# install AppData and add modalias provides
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 0644 %{SOURCE13} %{SOURCE15} %{buildroot}%{_datadir}/appdata/

# Man pages
mkdir -p %{buildroot}/%{_mandir}
rm -f doc/man/man1/cuda-install-samples-*
for man in doc/man/man{1,3,7}/*; do gzip -9 $man; done
cp -fr doc/man/* %{buildroot}/%{_mandir}
# This man page conflicts with *a lot* of other packages
mv %{buildroot}/%{_mandir}/man3/deprecated.3.gz \
    %{buildroot}/%{_mandir}/man3/cuda_deprecated.3.gz

# Docs
mv extras/CUPTI/Readme.txt extras/CUPTI/Readme-CUPTI.txt
mv extras/Debugger/Readme.txt extras/Debugger/Readme-Debugger.txt

# Base license file
mv samples/EULA.txt . 

# pkg-config files
install -d %{buildroot}/%{_libdir}/pkgconfig
install -m 644 %{_sourcedir}/*.pc  %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{cuda_lib}|g' -e 's|INCLUDE_DIR|%{cuda_include}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc %{buildroot}/%{cuda_bin}/nvcc.profile


  # Remove redundant man and samples
  rm -fr "%{buildroot}/opt/cuda/doc/man"
  rm -fr "%{buildroot}/opt/cuda/cuda-samples"
  rm -fr "%{buildroot}/usr/share/man/man3/deprecated.3"*

  # Remove included copy of java and link to system java
  rm -fr  "%{buildroot}/opt/cuda/jre"
  sed 's|../jre/bin/java|/usr/bin/java|g' \
    -i "%{buildroot}/opt/cuda/libnsight/nsight.ini" \
    -i "%{buildroot}/opt/cuda/libnvvp/nvvp.ini"

 # Remove unused files
  rm -fr "%{buildroot}/opt/cuda/"{bin,samples}"/.uninstall_manifest_do_not_delete.txt"
  rm -fr "%{buildroot}/opt/cuda/samples/uninstall_cuda_samples"*.pl
  rm -fr "%{buildroot}/opt/cuda/bin/cuda-install-samples"*.sh
  rm -fr "%{buildroot}/opt/cuda/bin/uninstall_cuda_toolkit"*.pl

%pre
# nothing

%postun 
#nothing

%files
%license pkg/EULA.txt
%{_sysconfdir}/ld.so.conf.d/cuda.conf
%{cuda_bin}/bin2c
%{cudadir}/nvvm/bin/cicc
# There should be no folder there, but binaries look for things here
%{cuda_bin}/crt/
%{cuda_bin}/cudafe++
%{cuda_bin}/cuobjdump
%{cuda_bin}/gpu-library-advisor
%{cuda_bin}/fatbinary
%{cuda_bin}/nvcc
%{cuda_bin}/nvcc.profile
%{cuda_bin}/nvlink
%{cuda_bin}/nvprune
%{cuda_bin}/ptxas
%{_mandir}/man1/cuda-binaries.*
%{_mandir}/man1/cuobjdump.*
%{_mandir}/man1/nvcc.*
%{_mandir}/man1/nvprune.*
%{cudadir}/nvvm/libdevice/libdevice.10.bc
%{cudadir}/version.txt
%dir %{cuda_data}/
%{cuda_data}/gdb/
%exclude %{cudadir}/extras/demo_suite/
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*sh

%files cli-tools
%{cuda_bin}/cuda-gdb
%{cuda_bin}/cuda-gdbserver
%{cuda_bin}/cuda-memcheck
%{cuda_bin}/nvdisasm
%{cuda_bin}/nvprof
%{_mandir}/man1/cuda-gdb.*
%{_mandir}/man1/cuda-gdbserver.*
%{_mandir}/man1/cuda-memcheck.*
%{_mandir}/man1/nvdisasm.*
%{_mandir}/man1/nvprof.*

%files libs
%license pkg/EULA.txt
%{cuda_lib}/libaccinj%{__isa_bits}.so.*
%{cuda_lib}/libcudart.so.*
%{cuda_lib}/libcuinj%{__isa_bits}.so.*
%{cudadir}/nvvm/%{_lib}/libnvvm.so.*
%{cuda_lib}/stubs/*.so
%{cuda_lib}/libnvjpeg.so.*
%{cuda_lib}/libOpenCL.so.*

%files cublas
%license pkg/EULA.txt
%{cuda_lib}/libcublas.so.*
%{cuda_lib}/libnvblas.so.*

%files cublas-devel
%{cuda_include}/cublas*
%{cuda_include}/nvblas*
#{cuda_lib}/libcublas_device.a
%{cuda_lib}/libcublas_static.a
%{cuda_lib}/libcublas.so
%{cuda_lib}/libnvblas.so
%{_libdir}/pkgconfig/cublas.pc

%files cudart
%license pkg/EULA.txt
%{cuda_lib}/libcudart.so.*

%files cudart-devel
%{cuda_include}/crt
%{cuda_include}/cuda_device_runtime_api.h
%{cuda_include}/cuda_runtime.h
%{cuda_include}/cuda_runtime_api.h
%{cuda_lib}/libcudadevrt.a
%{cuda_lib}/libcudart_static.a
%{cuda_lib}/libcudart.so
%{cuda_lib}/libculibos.a
%{_libdir}/pkgconfig/cudart.pc

%files nvtx
%license pkg/EULA.txt
%{cuda_lib}/libnvToolsExt.so.*

%files nvtx-devel
%{cuda_include}/nvToolsExt.h
%{cuda_include}/nvToolsExtCuda.h
%{cuda_include}/nvToolsExtCudaRt.h
%{cuda_include}/nvToolsExtMeta.h
%{cuda_include}/nvToolsExtSync.h
%{cuda_lib}/libnvToolsExt.so
%{_libdir}/pkgconfig/nvToolsExt.pc

%files cufft
%license pkg/EULA.txt
%{cuda_lib}/libcufft.so.*
%{cuda_lib}/libcufftw.so.*

%files cufft-devel
%{cuda_include}/cufft*
%{cuda_lib}/libcufft_static.a
%{cuda_lib}/libcufft_static_nocallback.a
%{cuda_lib}/libcufft.so
%{cuda_lib}/libcufftw_static.a
%{cuda_lib}/libcufftw.so
%{_libdir}/pkgconfig/cufft.pc

%files cupti
%license pkg/EULA.txt
%{cudadir}/extras/CUPTI/Readme.txt
%{cudadir}/extras/CUPTI/%{_lib}/libcupti.so.*

%files cupti-devel
%doc pkg/extras/CUPTI/Readme-CUPTI.txt
%{cudadir}/extras/CUPTI/include/
%{cudadir}/extras/CUPTI/%{_lib}/libcupti.so

%files curand
%license pkg/EULA.txt
%{cuda_lib}/libcurand.so.*

%files curand-devel
%{cuda_include}/curand*
%{cuda_include}/sobol_direction_vectors.h
%{cuda_lib}/libcurand_static.a
%{cuda_lib}/libcurand.so
%{_libdir}/pkgconfig/curand.pc

%files cusolver
%license pkg/EULA.txt
%{cuda_lib}/libcusolver.so.*

%files cusolver-devel
%{cuda_include}/cusolver*
%{cuda_lib}/libcusolver_static.a
%{cuda_lib}/libcusolver.so
%{_libdir}/pkgconfig/cusolver.pc

%files cusparse
%license pkg/EULA.txt
%{cuda_lib}/libcusparse.so.*

%files cusparse-devel
%{cuda_include}/cusparse*
%{cuda_lib}/libcusparse_static.a
%{cuda_lib}/libcusparse.so
%{cudadir}/src/cusparse_fortran.c
%{cudadir}/src/cusparse_fortran.h
%{cudadir}/src/cusparse_fortran_common.h
%{_libdir}/pkgconfig/cusparse.pc

%files npp
%license pkg/EULA.txt
%{cuda_lib}/libnpp*.so.*

%files npp-devel
%{cuda_include}/npp*
%{cuda_lib}/libnpp*_static.a
%{cuda_lib}/libnpp*.so
%{_libdir}/pkgconfig/npp.pc

%files nvgraph
%license pkg/EULA.txt
%{cuda_lib}/libnvgraph_static.a
%{cuda_lib}/libnvgraph.so.*

%files nvgraph-devel
%{cuda_include}/nvgraph*
%{cuda_lib}/libnvgraph.so
%{_libdir}/pkgconfig/nvgraph.pc

%files nvml-devel
%{cuda_include}/nvml*
%{cuda_lib}/stubs/libnvidia-ml.so
%{_libdir}/pkgconfig/nvml.pc

%files nvrtc
%license pkg/EULA.txt
%{cuda_lib}/libnvrtc-builtins.so.*
%{cuda_lib}/libnvrtc.so.*

%files nvrtc-devel
%{cuda_include}/nvrtc*
%{cuda_lib}/libnvrtc-builtins.so
%{cuda_lib}/libnvrtc.so
%{_libdir}/pkgconfig/nvrtc.pc

%files extra-libs
# Empty metapackage

%files devel
%doc pkg/extras/Debugger/Readme-Debugger.txt
%exclude %{cuda_include}/npp*
%exclude %{cuda_include}/nvgraph*
%exclude %{cuda_include}/sobol_direction_vectors.h
%exclude %{cuda_include}/nvrtc*
%exclude %{cuda_include}/nvml*
%exclude %{cuda_include}/cusparse*
%exclude %{cuda_include}/cusolver*
%exclude %{cuda_include}/curand*
%exclude %{cuda_include}/sobol_direction_vectors.h
%exclude %{cudadir}/extras/CUPTI/include
%exclude %{cuda_include}/cufft*
%exclude %{cuda_include}/nvToolsExt.h
%exclude %{cuda_include}/nvToolsExtCuda.h
%exclude %{cuda_include}/nvToolsExtCudaRt.h
%exclude %{cuda_include}/nvToolsExtMeta.h
%exclude %{cuda_include}/nvToolsExtSync.h
%exclude %{cuda_include}/crt
%exclude %{cuda_include}/cuda_device_runtime_api.h
%exclude %{cuda_include}/cuda_runtime.h
%exclude %{cuda_include}/cuda_runtime_api.h
%exclude %{cuda_include}/cublas*
%exclude %{cuda_include}/nvblas*
%{cuda_include}/
%{cudadir}/src/fortran.c
%{cudadir}/src/fortran.h
%{cudadir}/src/fortran_common.h
%{cudadir}/src/fortran_thunking.c
%{cudadir}/src/fortran_thunking.h
%{cudadir}/nvvm/include/nvvm.h
%{cuda_lib}/libaccinj%{__isa_bits}.so
%{cuda_lib}/libcuinj%{__isa_bits}.so
%{cudadir}/nvvm/%{_lib}/libnvvm.so
%{cuda_lib}/libOpenCL.so
%{cuda_lib}/libnvjpeg.so
%{cudadir}/extras/cuda-gdb-%{version}.src.tar.gz
%{cudadir}/extras/Debugger/
# static
%{cuda_lib}/liblapack_static.a
%{cuda_lib}/libmetis_static.a
%{cuda_lib}/libnvjpeg_static.a
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_libdir}/pkgconfig/cuda.pc

%files nsight-compute
%{cudadir}/NsightCompute-1.0/

%files docs
%doc pkg/doc/pdf/*.pdf pkg/doc/html/* pkg/tools/*
%{cuda_doc}/
%{cudadir}/tools/CUDA_Occupancy_Calculator.xls

%files samples
%{cudadir}/samples/
%{cudadir}/nvvm/libnvvm-samples/
%{cudadir}/extras/demo_suite/
%{cudadir}/nvml/example/
%{cudadir}/extras/CUPTI/sample/

%files nsight
%{cuda_bin}/nsight
%{cuda_bin}/nsight_ee_plugins_manage.sh
%if 0%{?fedora}
%{_datadir}/appdata/nsight.appdata.xml
%endif
%{_datadir}/applications/nsight.desktop
%{_datadir}/pixmaps/nsight.png
%{cudadir}/libnsight/
%{cudadir}/nsightee_plugins/com.nvidia.cuda.repo-1.0.0-SNAPSHOT.zip
%{_mandir}/man1/nsight.*

%files nvvp
%{cuda_bin}/computeprof
%{cuda_bin}/nvvp
%if 0%{?fedora}
%{_datadir}/appdata/nvvp.appdata.xml
%endif
%{_datadir}/applications/nvvp.desktop
%{_datadir}/pixmaps/nvvp.png
%{_mandir}/man1/nvvp.*
%{cudadir}/libnvvp/
%{cudadir}/libnvvp/nvvp

%changelog

* Mon Nov 12 2018 - David Vasquez <davidva AT tutanota DOT com>  10.0.130-1
- Updated to 10.0.130

* Mon Apr 16 2018 - David Vasquez <davidva AT tutanota DOT com>  9.1.85.2-1
- Initial release
