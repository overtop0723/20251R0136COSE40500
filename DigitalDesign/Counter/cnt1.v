module cnt1(CLK0, RST, out1);

output [3:0] out1;
input RST, CLK0;
reg [3:0] out0, temp_out0, out1, temp_out1;

always @(negedge RST or posedge CLK0)
  begin
    if(!RST)
      begin
        out0 <= 4'b0000;
        temp_out0 <= 4'b0001;
        out1 <= 4'b0000;
        temp_out1 <= 4'b0001;
      end
    else
      if(temp_out0 == 4'b1010)
        begin
          temp_out0 <= 4'b0001;
          out0 <= 4'b0000;
            
            if(temp_out1 == 4'b0000)
              begin
                temp_out1 <= 4'b0001;
                out1 <= 4'b0000;
              end
            else
              begin
              temp_out1 <= temp_out1 + 1;
              out1 <= temp_out1;
            end            
        end
      else
        begin
          temp_out0 <= temp_out0 + 1;
          out0 <= temp_out0;
        end
  end
  
endmodule