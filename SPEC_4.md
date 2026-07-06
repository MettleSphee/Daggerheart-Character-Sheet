#Ranger Beastbound subclass companion sheet for Daggerheart Character Sheet
I would like to add a group named Companion above the Advancement Points group in the Character Sheet.
This group shall only be visible whenever the selected subclass (whether it's for the main class or the multiclass) is Beastbound. This implies that the selected main class or multiclass must be Ranger.
The Companion group (titled Companion) shall contain the following fields, separated by ###Rows and, where applicable, ###Columns:

###Row 1
(((Text Field))) with the above text "Companion Name";
(((Number field))) with the above text "Evasion", text contains tooltip "Start at 10";

###Row 2
(((Text Field))) "Species"
(((Text Field))) "Describe your companion"

###Row 3
(((Text))) "Work with the GM to decide what kind of animal you have as your companion. Give them a name and draw or
attach a picture of them in the space above. Then create two Experiences for your companion based on their
training and the history you have together. Finally, describe their method of dealing damage (their standard
attack) and record it in the “Attack & Damage” section. Their damage starts at d6 and their range starts at Melee."

###Row 4
(((Title))) "Companion Experience"
###Column 1
(((Text))) "Start with +2 in two Experiences. Whenever you gain a new Experience,
your companion also gains one. All new Experiences start at +2."
#### 5 subrows containing the same thing (different instances) in the Column 1
(((Text Field))) (((Number Field)))
###Column 2
(((Text))) "**Example Companion Experiences**\n\nBold Distraction, Expert Climber, Fetch, Friendly, Guardian of the Forest, Horrifying, Intimidating, Loyal Until the End, Navigation, Nimble, Nobody Left Behind, On High Alert, Protective, Royal Companion, Scout, Service Animal, Trusted Mount, Vigilant, We Always Find Them, You Can’t Hit What You Can’t Find"

###Row 5
(((Text))) "Make a **Spellcast Roll** to connect with your companion and command them to take action. **Spend a Hope** to add an applicable Companion Experience to the roll. On a success with Hope, if your next action builds on their success, you gain advantage on the roll."

###Row 6
###Column 1, items are separated by sub-rows when the $ character is present in this SPEC;
(((Title))) "Attack & Damage"$
(((Text Field))) "Standard Attack"
(((Drop-down))) "Range" - Populated by the items ["Melee","Very Close","Close","Far","Very Far"]$
(((Checkmark))) D6
(((Checkmark))) D8
(((Checkmark))) D10
(((Checkmark))) D12
####Constraint: Only one checkmark can be selected from the 4 above at the time
$
(((Text))) "When you command your companion to attack, they gain any benefits that would normally only apply to you (such as the effects of \"Ranger’s Focus\"). On a success, their damage roll uses your Proficiency and their damage die."
$
(((Title))) "Stress"$
(((Number Field, limit 6))) "Stress"
(((Checkmarks equal to Number Field above))) "Marked Stress"$
(((Text))) "When your companion would take any amount of damage, they mark a Stress. When they mark their last Stress, they drop out of the scene (by hiding, fleeing, or a similar action).\nThey remain unavailable until the start of your next long rest, where they return with 1 Stress cleared.\nWhen you choose a downtime move that clears Stress on yourself, your companion clears an equal number of Stress."

###Column 2, items are separated by sub-rows when the $ character is present in this SPEC;
(((Title))) "Training"$
(((Text)))"When your character levels up, choose one available option for your companion from the following list and mark it here."$
(((3 checkmarks))) "**Intelligent**: Your companion gains a permanent +1 bonus to a Companion Experience of your choice."$
(((Checkmark))) "**Light in the Dark:**" (((Checkmark))) "Use this as an additional Hope slot your character can mark."$
(((Checkmark))) "**Creature Comfort**: Once per rest, when you take time during a quiet moment to give your companion love and attention, you can gain a Hope or you can both clear a Stress."$
(((Checkmark))) "**Armored**: When your companion takes damage, you can **mark one of your Armor Slots** instead of marking one of their Stress."$
(((3 checkmarks))) "**Vicious**: Increase your companion’s damage dice or range by one step (d6 to d8, Close to Far, etc.)."
(((3 checkmarks))) "**Resilient**: Your companion gains an additional Stress slot."
(((Checkmark))) "**Bonded**: When you mark your last Hit Point, your companion rushes to your side to comfort you. Roll a number of **D6s** equal to the unmarked Stress slots they have and mark them. If any roll a 6, your companion helps you up. Clear your last Hit Point and return to the scene."
(((3 checkmarks))) "**Aware**: Your companion gains a permanent +2 bonus to their Evasion."

