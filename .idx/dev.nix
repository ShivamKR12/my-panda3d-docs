{ pkgs, ... }:

let
  ps = pkgs.python311Packages;

  exhale = ps.buildPythonPackage rec {
    pname = "exhale";
    version = "0.3.7";
    src = pkgs.fetchurl {
      url = "https://files.pythonhosted.org/packages/2f/2b/c5c665e743415c894d49c60e7b1338fb86d05c9ec8909a38e700e55626f0/exhale-0.3.7.tar.gz";
      sha256 = "1n5hsrg7swh535bd5b3f55ldcb343yld849kjcfm2mlllp89cakm";
    };
    format = "setuptools"; # exhale uses setup.py; safe to declare
    doCheck = false;
    
    # 👇 ADD `ps.six` here
    propagatedBuildInputs = [ ps.sphinx ps.breathe ps.six ps.beautifulsoup4 ];
  };

in
{
  channel = "stable-24.05";

  packages = with pkgs; [
    python3
    ps.pip
    ps.sphinx
    ps.breathe
    exhale

    doxygen
    graphviz
    gnumake
    git
    gitAndTools.github-cli
  ];

  idx = {
    extensions = [
      "ms-python.python"
      "ms-vscode.cpptools"
      "ms-vscode.cmake-tools"
      "cschlosser.doxdocgen"
      "yzhang.markdown-all-in-one"
      "joaompinto.vscode-graphviz"
    ];

    previews = {
      enable = true;
      previews = {};
    };

    workspace = {
      onCreate = {};
      onStart = {};
    };
  };
}
