module cnt0(CLK0, RST, out0);

output [3:0] out0;
input RST, CLK0;
reg [3:0] out0, temp_out0;

always @(negedge RST or posedge CLK0)
  begin
    if(!RST)
      begin
        temp_out0 <= 4'b0001;
        out0 <= 4'b0000;
      end
    else
      if(temp_out0 == 4'b0000)
        begin
          temp_out0 <= 4'b0001;
          out0 <= 4'b0000;
        end
      else
        begin
          temp_out0 <= temp_out0 + 1;
          out0 <= temp_out0;
        end
  end
  
endmodule
