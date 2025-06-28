let
  pkgs = import <nixpkgs> {};
  devEnv = import ./.idx/dev.nix {
    inherit pkgs;
  };
in
pkgs.mkShell {
  buildInputs = devEnv.packages;
}
