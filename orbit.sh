#!/bin/bash

# orbit.sh

# ./orbit.sh restart
# ./orbit.sh setup devel
# ./orbit.sh setup devel  --new
# ./orbit.sh setup devel  --only-symlink
# ./orbit.sh setup devel  --only-uv-init
# ./orbit.sh tools up
# ./orbit.sh tools down

FLET_VER="{{ flet_version }}"

COMMAND="${1:-none}"
SUBCOMMAND="${2:-none}"
OPTION="${3:-none}"


# CLI Router

case $COMMAND in

  help)
    echo "Help"
    ;;

  restart)
    echo "restart"
    ;;

  setup)
    echo "Setup"
    ;;

  tool | tools)
    echo "Tools"
    if [ $2 == "up" ]
    then
      echo "Tools UP"
    elif [ $2 == "down" ]
    then
      echo "Tools DOWN"
    else
      echo "Tools Usage"
    fi
    ;;

  *)
    echo "Usage"
    ;;
esac

# Command functions

# Atomic functions
