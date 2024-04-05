# WARNING: This file was automatically generated. You should avoid editing it.
# If you run pynixify again, the file will be either overwritten or
# deleted, and you will lose the changes you made to it.

{ anyascii, buildPythonPackage, fetchPypi, lib }:

buildPythonPackage rec {
  pname = "filedepot";
  version = "0.11.0";

  src = fetchPypi {
    inherit pname version;
    sha256 = "15f1mmm3psv60z7r03933kfs16fn5gwx396vvfs8zw43fdjcmm16";
  };

  propagatedBuildInputs = [ anyascii ];

  # TODO FIXME
  doCheck = false;

  meta = with lib; {
    description =
      "Toolkit for storing files and attachments in web applications";
    homepage = "https://github.com/amol-/depot";
  };
}
