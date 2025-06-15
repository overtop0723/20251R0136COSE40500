// Full Adder

module full_adder(x, y, c_in, s_out, c_out);

input x, y, c_in;
output s_out, c_out;

wire temp_sum, temp_carry_1, temp_carry_2;

half_adder U0(.x(x), .y(y), .s(temp_sum), .c(temp_carry_1));
half_adder U1(.x(temp_sum), .y(c_in), .s(s_out), .c(temp_carry_2));
or2 U2(.x(temp_carry_2), .y(temp_carry_1), .o(c_out));

endmodule