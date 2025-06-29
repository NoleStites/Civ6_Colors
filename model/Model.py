from os import remove

class Model():

    def reset_files(self, leader_dict):
        """
        This method will remove all colors created by this application
        and assign a new default value to all affected Alt3s.
        """
        color_path = "C:\\Program Files (x86)\\Steam\steamapps\\common\\Sid Meier's Civilization VI\\Base\\Assets\\UI\\Colors\\"

        # Reset the global colors
        original = open(color_path+"PlayerStandardColors.xml", "r")
        new_copy = open(color_path+"Copy_PlayerStandardColors.xml", "w")

        # Figure out how many colors need to be removed during copy process
        counter = 1
        entry_count = 0
        for line in original:
            if counter != 5:
                new_copy.write(line)
                counter += 1
                continue
            
            temp_line = line
            temp_line.lstrip()
            temp_line = temp_line.split("_")[-1]
            temp_line = temp_line.replace("</Type>\n", "")
            try:
                entry_count = int(temp_line)
            except:
                new_copy.write(line)
                entry_count = 0
                counter += 1
                continue
            new_copy.write(line)
            counter += 1

        original.close()
        new_copy.close()

        # Move copy file contents into original, skipping entry_count*4 lines
        original = open(color_path+"PlayerStandardColors.xml", "w")
        new_copy = open(color_path+"Copy_PlayerStandardColors.xml", "r")
        
        entry_count *= 4
        counter = 1
        for line in new_copy:
            if counter == 4:
                if entry_count != 0:
                    entry_count -= 1
                    continue

            original.write(line)
            counter += 1

        original.close()
        new_copy.close()
        remove(color_path+"Copy_PlayerStandardColors.xml")

        # Reset red and white to all Alt3s as default
        default_primary = "COLOR_STANDARD_RED_MD"
        default_secondary = "COLOR_STANDARD_WHITE_LT"
        tuple_list = leader_dict.items()
        for leader_path in tuple_list:
            self.assign_alt3(leader_path[0], leader_path[1], default_primary, default_secondary)


    def assign_alt3(self, leader, path, p_title, s_title):
        """
        Will search for 'leader' in the file at the end of the
        'path'. Once located, this method will assign new primary
        and secondary values to the Alt3 color of that leader.
        """
        # Reformat the leader string to fit the contents of the file
        caps_leader = leader.upper().replace(" ", "_")
        caps_leader = "LEADER_" + caps_leader

        # Open and prepare the file at the end of the given path
        copy_path = path.split("\\")
        copy_path.pop(-1)
        new_path = ""
        for segment in copy_path:
            new_path += segment + "\\"
        new_path += "temp.xml"
        
        original = open(path, "r")
        new_copy = open(new_path, "w")

        # As we copy original to copy, keep track of where leader is
        leader_location = None
        counter = 1
        for line in original:
            new_copy.write(line)
            if line.find(caps_leader) != -1:
                leader_location = counter
            counter += 1

        original.close()
        new_copy.close()

        # Move copy into original and write over Alt3 at leader_location
        original = open(path, "w")
        new_copy = open(new_path, "r")
        
        finished = False
        counter = 1
        for line in new_copy:
            if counter <= leader_location or finished == True:
                original.write(line)
                counter += 1
                continue
            
            new_line = line

            if line.find("Alt3Primary") != -1:  # Assign primary color
                new_line = new_line[0:21] + p_title + "</Alt3PrimaryColor>\n"
            elif line.find("Alt3Secondary") != -1: # Assign secondary color
                new_line = new_line[0:23] + s_title + "</Alt3SecondaryColor>\n"
                finished = True

            original.write(new_line)
            counter += 1
        
        original.close()
        new_copy.close()
        remove(new_path)
        


    def add_colors(self, primary_rgb, secondary_rgb):
        """
        Will add the given primary and secondary rgb values
        to the global list of colors for use by the leaders.
        """
        color_path = "C:\\Program Files (x86)\\Steam\steamapps\\common\\Sid Meier's Civilization VI\\Base\\Assets\\UI\\Colors\\"
        
        # Create a copy of the original file
        original = open(color_path+"PlayerStandardColors.xml", "r")
        new_copy = open(color_path+"Copy_PlayerStandardColors.xml", "w")

        counter = 1
        max_color = 0
        for line in original:
            new_copy.write(line)
            temp_line = ""
            for ch in line:
                temp_line += ch
            if counter == 5:
                if temp_line.find("NEW_COLOR_") != -1:
                    y = temp_line.split("_")[2]
                    max_color = int(y.split("<")[0])
            counter += 1

        original.close()
        new_copy.close()

        # Write to the original by using the copy and editing what needs to be editted
        original = open(color_path+"PlayerStandardColors.xml", "w")
        new_copy = open(color_path+"Copy_PlayerStandardColors.xml", "r")

        counter = 1
        for line in new_copy:
            if counter != 4:
                original.write(line)
            else:
                pri_sec = (primary_rgb, secondary_rgb)
                for i in range(2, 0, -1): # One for primary, one for secondary
                    if i == 1:
                        primary_num = max_color + i
                    elif i == 2:
                        secondary_num = max_color + i
                    temp1 = f"\t\t\t<Type>NEW_COLOR_{max_color + i}</Type>\n"
                    temp2 = f"\t\t\t<Color>{pri_sec[i-1][0]},{pri_sec[i-1][1]},{pri_sec[i-1][2]},255</Color>\n"
                    color_template = [
                    "\t\t<Row>\n",
                    temp1,
                    temp2,
                    "\t\t</Row>\n"
                    ]
                    for new_line in color_template:
                        original.write(new_line)
                original.write(line)

            counter += 1

        original.close()
        new_copy.close()
        remove(color_path+"Copy_PlayerStandardColors.xml")

        primary_title = f"NEW_COLOR_{primary_num}"
        secondary_title = f"NEW_COLOR_{secondary_num}"
        return primary_title, secondary_title



    def acquire_leaders(self):
        """
        Responsible for going directly into the
        Civ 6 files and extracting the leader
        names as strings.
        """
        # File path to base of civ files
        # \Program Files (x86)\Steam\steamapps\common\Sid Meier's Civilization VI

        all_leaders = []

        # Get list of Base Leaders
        base_leaders, base_dict = self.get_base_leaders()
                
        # Get DLC Leaders
        dlc_leaders, dlc_dict = self.get_dlc_leaders()

        # Sort the results
        base_leaders.extend(dlc_leaders)
        for leader in base_leaders:
            all_leaders.append(leader)

        # Combine the dictionaries
        dlc_list = dlc_dict.items()
        for tup in dlc_list:
            base_dict[tup[0]] = tup[1]

        return all_leaders, base_dict


    def get_dlc_leaders(self):
        # Create file paths to search for
        civs = [
            "Australia",
            "Aztec_Montezuma",
            "Byzantium_Gaul",
            "CatherineDeMedici",
            "Ethiopia",
            "GranColombia_Maya",
            "GreatBuilders",
            "GreatNegotiators",
            "GreatWarlords",
            "Indonesia_Khmer",
            "JuliusCaesar",
            "KublaiKhan_Vietnam",
            "Macedonia_Persia",
            "Nubia_Amanitore",
            "Poland_Jadwiga",
            "Portugal",
            "RulersOfChina",
            "RulersOfEngland",
            "RulersOfTheSahara",
            "TeddyRoosevelt",
            "Expansion1",
            "Expansion2",
            "Babylon"
        ]
        
        files_to_search = []
        for civ in civs:
            if civ == "Nubia_Amanitore":
                end = civ.replace("_Amanitore", "")
                files_to_search.append(f"{civ}\\Data\\{end}_PlayerColors.xml")
            elif civ == "Macedonia_Persia":
                files_to_search.append(f"{civ}\\Data\\{civ}_PlayerColors.xml")
            elif civ == "Expansion1":
                files_to_search.append(f"{civ}\\Data\\{civ}_PlayerColors.xml")
            elif civ == "Expansion2":
                files_to_search.append(f"{civ}\\Data\\{civ}_PlayerColors.xml")
            elif civ == "Babylon":
                files_to_search.append(f"{civ}\\Data\\{civ}_Colors_Config.xml")
            else:
                files_to_search.append(f"{civ}\\Data\\{civ}_Colors.xml")

        # Add the leaders that the user owns to a list to be returned
        dlc_leaders = []
        dlc_leaders_dict = {}

        for filepath in files_to_search:
            try:
                f = open(f"C:\\Program Files (x86)\\Steam\steamapps\\common\\Sid Meier's Civilization VI\\DLC\\{filepath}", "r")
            except:
                temp = filepath.split("\\")
                print(f"You don't have {temp[0]}.")
                continue
            
            for line in f:
                if line.find("LEADER") != -1:
                    line = line.lstrip().replace("<Type>LEADER_", "").replace("</Type>", "").replace("\n", "").replace("_", " ")
                    line = line.lower().title()
                    if line == "Joao Iii":
                        line = line.replace("Iii", "III")
                    dlc_leaders.append(line)
                    dlc_leaders_dict[line] = f"C:\\Program Files (x86)\\Steam\steamapps\\common\\Sid Meier's Civilization VI\\DLC\\{filepath}"
            f.close()
        
        return dlc_leaders, dlc_leaders_dict

    
    def get_base_leaders(self):
        try:
            f = open("C:\\Program Files (x86)\\Steam\steamapps\\common\\Sid Meier's Civilization VI\\Base\\Assets\\UI\\Colors\\PlayerColors.xml", "r")
        except:
            print("PlayerColors.xml doesn't exist!")

        leader_list = []
        leader_path_dict = {}

        for line in f:
            if line.find("LEADER") != -1:
                line = line.lstrip().replace("<Type>LEADER_", "").replace("</Type>", "").replace("\n", "").replace("_", " ")
                line = line.lower().title()
                if line == "Philip Ii":
                    line = line.replace("Ii", "II")
                leader_list.append(line)
                leader_path_dict[line] = "C:\\Program Files (x86)\\Steam\steamapps\\common\\Sid Meier's Civilization VI\\Base\\Assets\\UI\\Colors\\PlayerColors.xml"
        f.close()
        return leader_list, leader_path_dict
    

    def create_global_color(self, rgb_values):
        """
        Given a tuple of rgb values, this method will
        create a new global color in PlayerStandardColors.xml.
        """
        r = rgb_values[0]
        g = rgb_values[1]
        b = rgb_values[2]
        template_string = f"<Row>\n    <Type>NEW_COLOR_A</Type>\n    <Color>{r},{g},{b},255</Color>\n</Row>\n"
        print(template_string)

