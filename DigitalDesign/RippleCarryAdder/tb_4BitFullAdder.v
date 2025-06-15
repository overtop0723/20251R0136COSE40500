`timescale 1ns/1ns

module tb_RCA4bit;
reg [3:0] x;
reg [3:0] y;
reg c_in;
wire [3:0] sum;
wire c_out;

RCA4Bit Adder (x, y, c_in, sum, c_out);

initial
begin

x = 4'b0000; y=4'b0000; c_in=0;
#100; x = 4'b0001; y=4'b0001; c_in=0;
#100; x = 4'b0010; y=4'b0001; c_in=0;
#100; x = 4'b0011; y=4'b0011; c_in=0;
#100; x = 4'b0100; y=4'b0011; c_in=0;
#100; x = 4'b0111; y=4'b0110; c_in=0;
#100; x = 4'b1000; y=4'b0111; c_in=0;
#100; x = 4'b1111; y=4'b1111; c_in=0; // '1111' + '1111' + '0'
end
endmodule