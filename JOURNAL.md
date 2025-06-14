---
Title: "Custom DIY Keyboard"
Author: "@ORION"
Description: "Documenting my journey of making a custom DIY Keyboard"
Created_at: "2025-06-10"
---

# Journal Starts Here!!

# June 11: Github Setup!
Setup up the github for the DIY Custom keyboard, So I can document my progress

### Total Time Spent: N/A

# June 12: Learning Keyboard Schematics and Core functionality

Today I was thinking of getting started on the schematic but then realized that It wont be as easy as making a macropad. So I had to learn about switch matrix and how to efficiently use GPIO pins on the MCU to maximize the utility and how to properly make the schematic for a mechanical keyboard and what parts I should choose based on the requirements and the wants of my keyboards(Rotary Encoder and Oled Display). I watched a couple of youtube videos to learn about it and I also learnt about some cool plugins(e.g key switch plugin) I can use in KiCad to make it easier to design the schematic and make the process faster

After learning about the schematics, I started making a list of things that I want in my keyboard and the things I have will need to make it happen. Check out the Link to see the core functionality of my keyboard and what parts I will be using.
[Click Here!!](https://docs.google.com/document/d/16dAgHImxQ1OMsn2_r7Q9AnMd_Z1fVW2yfl9RcRUop_U/edit?usp=sharing)

Tomorrow I will get started on the schematic and hopefully finish!

### Total Time Spent: 2 Hours

# June 13: Finished Schematics

Today I started by setting up KiCad by adding symbol and footprint libraries (Thanks to Joe Scotto for making an awesome collection of libraries) [Libraries](https://github.com/joe-scotto/scottokeebs). After Successfully adding the libraries to KiCad. I moved on to working on the Schematic for the custom keyboard with 61 Keys, 1 rotary encoder and an oled screen. For the schematic, I started with the switch matrix.

Below is the Switch Matrix I made at first
![first_matrix_image](https://github.com/rakshitDarji007/CustomDIY_Keyboard/blob/main/Images/Screenshot%202025-06-13%20120938.png)

After making this matrix I realized that this is a very bad layout and the norm is to have the same amount of columns as the rows. So then I decided to change the matrix to meet the standard
![Second_Matrix_image](https://github.com/rakshitDarji007/CustomDIY_Keyboard/blob/main/Images/Screenshot%202025-06-13%20122407.png)

Now that I had the matrix done, I started working on adding the MCU. When adding the MCU I was gonna use the RP2040 but then realized that using a bare chip is a very complicated for a beginner like me, so I asked in slack for help and got feedback to use a board like the raspberry Pi Pico. After deciding on the MCU that I will use(Pi Pico) I finished connecting everything to the MCU(Switch Matrix, Rotary Encoder, and Oled Screens)
![alt_text](https://github.com/rakshitDarji007/CustomDIY_Keyboard/blob/main/Images/Screenshot%202025-06-13%20171404.png)

Moving on, I ran the footprint assingment tool and assigned the footprints but accidently assigned the wrong footprint for the switches which gave me errors when updating the PCB from the schematic in the PCB editor so wasted a lot of time looking for what was wrong. Eventually I retraced the steps and checked everything from the start and realized I had assigned the wrong footprints for the switches(assigned CAD footprints instead of PCB_MX😭)

After fixing the the footprint problems, I moved on to the PCB editor, then imported the PCB from the schematic and it imported with 0 errors!.
![pcb_editor_image](https://github.com/rakshitDarji007/CustomDIY_Keyboard/blob/main/Images/Screenshot%202025-06-13%20175918.png)

### Time Spent(Current Session): 4.5 Hours
### Total Time Spent: 6.5 Hours
