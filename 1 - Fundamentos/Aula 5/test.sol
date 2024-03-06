// O contrato de teste simula o mesmo contrato do script.sol com a função flip.
// Os scripts de teste rodam as mesmas funções dos scripts, mas em um documento isolado exclusivo para visibilidade de resultados.

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import {Test} from "forge-std/Test.sol";
import {Flipper} from "../src/Flipper.sol";

contract FlipperTest is Test {
    Flipper public flipper;

    function setUp() public {
        flipper = new Flipper();
    }

    function test_getValue() public {
        assertEq(flipper.getValue(), true);
    }

    function test_flipValue() public {
        flipper.flip();
        assertEq(flipper.getValue(), false);
    }

    function test_flipDataValue() public {
        assertEq(flipper.getData(98), address(0x2));
    }
}
