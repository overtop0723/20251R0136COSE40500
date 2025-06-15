// 4-Bit Full Adder

module RCA4Bit (x, y, c_in, sum, c_out);

input [3:0] x, y;
input c_in;
output [3:0] sum;
output c_out;

wire c_in1, c_in2, c_in3;

full_adder U0 (x[0], y[0], c_in, sum[0], c_in1);
full_adder U1 (x[1], y[1], c_in1, sum[1], c_in2);
full_adder U2 (x[2], y[2], c_in2, sum[2], c_in3);
full_adder U3 (x[3], y[3], c_in3, sum[3], c_out);

endmodule
