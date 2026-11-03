// Simulation of Logic Gates - AND, OR, XOR

module and_gate_level(input a, input b, output y);
    and (y, a, b);
endmodule

module or_gate_level(input a, input b, output y);
    or (y, a, b);
endmodule

module xor_gate_level(input a, input b, output y);
    xor (y, a, b);
endmodule
