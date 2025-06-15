`timescale 1ns/1ns

module tb_clk();
reg CLK0, RST;
wire [3:0] out0, out1, out2, out3;

cnt0 Cnt0 (CLK0, RST, out0);
cnt1 Cnt1 (CLK0, RST, out1);
cnt2 Cnt2 (CLK0, RST, out2);
cnt3 Cnt3 (CLK0, RST, out3);

initial
begin
  CLK0 = 1;
  forever #500 CLK0 = ~CLK0; 
end

initial
begin
  RST = 0;
  #200 RST = 1;
end

endmodule
