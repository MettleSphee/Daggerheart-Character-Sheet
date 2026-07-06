#Three Column Group for Daggerheart Character Sheet
Please add a three-column group to the character sheet and integrate it with the rest of the character sheet (including saving the fields and their values); In the following notation, the columns will be marked as "#Column <number>, with the number representing 1-3, or the order (from left to right) of the columns. These are NOT titles, but only a notation format that will be followed for implementing it. Checkmarks will be noted in front of each row that needs it, with text following it, in the notation (<X>) "<Text>", where X represents the number of checkmarks, and Text represents the text of that row. Each column will have fields, separated by rows defined as follows:

##Column 1:
Title: "Tier 2: Levels 2-4"
Text: "At level 2, gain an additional Experience at +2 and gain a +1 bonus to your Proficiency."
Text: "Choose two options from the list below and mark them."
(3) "Gain a +1 bonus to two unmarked character traits and mark them."
(2) "Permanently gain one HP slot."
(2) "Permanently gain one Stress slot."
(1) "Permanently gain a +1 bonus to two Experiences."
(1) "Choose an additional domain card of your level or lower from a domain you have access to (up to level 4)."
(1) "Permanently gain a +1 bonus to your Evasion."

##Column 2:
Title: "Tier 3: Levels 5-7"
Text: "At level 5, gain an additional Experience at +2 and clear all marks on character traits. Then gain a +1 bonus to your Proficiency."
Text: "Choose two options from the list below or any from the previous tier and mark them."
(3) "Gain a +1 bonus to two unmarked character traits and mark them."
(2) "Permanently gain one HP slot."
(2) "Permanently gain one Stress slot."
(1) "Permanently gain a +1 bonus to two Experiences."
(1) "Choose an additional domain card of your level or lower from a domain you have access to (up to level 7)."
(1) "Permanently gain a +1 bonus to your Evasion."
(1) "Take an upgraded subclass card. Then cross out the multiclass option for this tier."
(2) "Increase your Proficiency by +1."
(2) "Multiclass: Choose an additional class for your character, then cross out an unused 'Take an upgraded subclass card' and the other multiclass option on this sheet."

##Column 3:
Title: "Tier 4: Levels 8-10"
Text: "At level 8, gain an additional Experience at +2 and clear all marks on character traits. Then gain a +1 bonus to your Proficiency."
Text: "Choose two options from the list below or any from the previous tier and mark them."
(3) "Gain a +1 bonus to two unmarked character traits and mark them."
(2) "Permanently gain one HP slot."
(2) "Permanently gain one Stress slot."
(1) "Permanently gain a +1 bonus to two Experiences."
(1) "Choose an additional domain card of your level or lower from a domain you have access to (up to level 7)."
(1) "Permanently gain a +1 bonus to your Evasion."
(1) "Take an upgraded subclass card. Then cross out the multiclass option for this tier."
(2) "Increase your Proficiency by +1."
(2) "Multiclass: Choose an additional class for your character, then cross out an unused 'Take an upgraded subclass card' and the other multiclass option on this sheet."


After the columns, in the same group, add the following row:
Text: "Update your level and adjust your damage thresholds accordingly. Take an additional domain card of your level or lower from a domain you have access to."

Please add the following logic to the items in the columns:
- On tier 3 and 4 columns, the checkmarks for upgraded subclass shall disable the multiclass checkmarks in their respective tiers. The checkmarks and text shall be grayed out to mark that they are disabled;
- On tier 3 and 4 columns, the checkmarks for multiclass shall disable the multiclass checkmarks in the other tier. These shall also disable the upgraded subclass checkmark for their respective tier. The checkmarks and text shall be grayed out to mark that they are disabled;
- On tier 3 and 4 columns, the checkmarks for Proficiency and Multiclass shall have a border grouping the checkmarks. The border shall be thickened slightly, so that it marks a requirement to take both of them.
- On tier 3 and 4 columns, the checkmarks for Proficiency shall disable the Proficiency checkmarks on the other tier. The checkmarks and text shall be grayed out to mark that they are disabled;
