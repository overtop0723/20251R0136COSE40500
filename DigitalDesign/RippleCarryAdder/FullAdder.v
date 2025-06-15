// Full Adder

module full_adder(x, y, c_in, s_out, c_out);

input x, y, c_in;
output s_out, c_out;
reg s_out, c_out;

always @(x or y or c_in)
begin

if(x==1'b0 && y==1'b0 && c_in==1'b0)
begin
s_out = 0; c_out=0;
end

if(x==1'b0 && y==1'b0 && c_in==1'b1)
begin
s_out = 1; c_out=0;
end

if(x==1'b0 && y==1'b1 && c_in==1'b0)
begin
s_out = 1; c_out=0;
end

if(x==1'b0 && y==1'b1 && c_in==1'b1)
begin
s_out = 0; c_out=1;
end

if(x==1'b1 && y==1'b0 && c_in==1'b0)
begin
s_out = 1; c_out=0;
end

if(x==1'b1 && y==1'b0 && c_in==1'b1)
begin
s_out = 0; c_out=1;
end

if(x==1'b1 && y==1'b1 && c_in==1'b0)
begin
s_out = 0; c_out=1;
end

if(x==1'b1 && y==1'b1 && c_in==1'b1)
begin
s_out = 1; c_out=1;
end

end

endmodule