`timescale 1ns / 1ps
module testbench;

	parameter N1 = 8;
 // input width
	parameter N2 = 16;
    // output width
	parameter N3 = 32;
	
reg CLK;
reg RST;
reg ENABLE;

reg [N2-1:0] input_data;

reg [N2-1:0] data[99:0];

wire [N3-1:0] ouput_data;

wire [N2-1:0] sampleT;

fir_filter UUT(.input_data(input_data),
					.output_data(output_data),
					.CLK(CLK),
					.RST(RST),
					.ENABLE(ENABLE),
					.sampleT(sampleT)
					);
					
integer k;

integer FILE1;

always #10 CLK=~CLK;

initial
begin
		k=0; //the row that the program will start reading from
		
		$readmemb("input.data", data);
		
		
		FILE1=$fopen("save.data","w");
		
		//set the clock to zero
		CLK = 0;
		#20
		
		//reset the filter
		RST=1'b1;
		#40
		
		//enabling the filter
		RST=1'b0;
		ENABLE = 1'b1;
		input_data <= data[0];
		#10
		
		//for loop to read all lines of the input.data file
		for (k=1; k<100; k=k+1)
		begin
				@(posedge CLK);
				$fdisplay(FILE1, "%b", output_data);
				input_data <= data[k];
				if (k==99) //close file after reading final line
				$fclose(FILE1);
			end
	end
	endmodule
				
