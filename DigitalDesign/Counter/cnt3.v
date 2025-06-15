module cnt3(CLK0, RST, out3);

output [3:0] out3;
input RST, CLK0;
reg [3:0] out0, temp_out0, out1, temp_out1, out2, temp_out2, out3, temp_out3;

always @(negedge RST or posedge CLK0)
  begin
    if(!RST)
      begin
        out0 <= 4'b0000;
        temp_out0 <= 4'b0001;
        out1 <= 4'b0000;
        temp_out1 <= 4'b0001;
        out2 <= 4'b0000;
        temp_out2 <= 4'b0001;
        out3 <= 4'b0000;
        temp_out3 <= 4'b0001;
      end
    else
      if(temp_out0 == 4'b1010)
        begin
          temp_out0 <= 4'b0001;
          out0 <= 4'b0000;
            
            if(temp_out1 == 4'b1010)
              begin
                temp_out1 <= 4'b0001;
                out1 <= 4'b0000;

                if(temp_out2 == 4'b1010)
                  begin
                    temp_out2 <= 4'b0001;
                    out2 <= 4'b0000;

                      if(temp_out3 == 4'b0000)
                        begin
                          temp_out3 <= 4'b0001;
                          out3 <= 4'b0000;
                        end
                      else
                        begin
                          temp_out3 <= temp_out3 + 1;
                          out3 <= temp_out3;
                        end
                  end
                else
                  begin
                    temp_out2 <= temp_out2 + 1;
                    out2 <= temp_out2;
                  end
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

