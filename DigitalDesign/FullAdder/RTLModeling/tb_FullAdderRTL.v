// Test Bench - FullAdder
`timescale 1ns/1ns

module tb_FullAdder();

reg x, y, c_in;
wire s_out, c_out;

full_adder TB (.x(x), .y(y), .c_in(c_in), .s_out(s_out), .c_out(c_out));

initial
begin
x=0; y=0; c_in=0;
#100; x=0; y=0; c_in=1;
#100; x=0; y=1; c_in=0;
#100; x=0; y=1; c_in=1;
#100; x=1; y=0; c_in=0;
#100; x=1; y=0; c_in=1;
#100; x=1; y=1; c_in=0;
#100; x=1; y=1; c_in=1;
end

endmodule
