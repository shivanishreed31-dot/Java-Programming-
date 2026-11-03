module jay(
    input din,
    input s1, s0,
    output reg y0, y1, y2, y3
);

always @(*) begin
    y0 = 0;
    y1 = 0;
    y2 = 0;
    y3 = 0;

    if (s1 == 0 && s0 == 0)
        y0 = din;
    else if (s1 == 0 && s0 == 1)
        y1 = din;
    else if (s1 == 1 && s0 == 0)
        y2 = din;
    else
        y3 = din;
end

endmodule
