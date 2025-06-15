// Half Adder

module half_adder(x, y, s, c);

input x, y;
output s, c;
reg s, c;

always @(x or y)
begin
if((x==2'b1 && y==2'b0) || (x==2'b0 && y==2'b1)) s=1;
else s=0;
end

always@(x or y)
begin
if(x==2'b1 && y==2'b1) c=1;
else c=0;
end

endmodule