While creating and evaluating example USLM markup of the Boston municipal and Uniform laws Shreyash and I discussed how best to simplify the USLM vocabulary to make it more usable and understandable.  Shreyash indicated that the four most important tags applicable to "black letter law" (the actual substantive law, not the notes or procedural content) seem to be:

* Heading
* Level
* Num
* Text

We went through the entire documentation of USLM (using their USLM User Guide) and re-confirmed his insight.  While there are many other tags and processes of importance, the irreducible subset appear to be the above four.  

My own goal is for all people - even those in middle school - to be able to read and understand at least simple version of the actual law in it's machine readable and human readable forms.  It is important to express the four key elements in the simplest possible manner that still retains their functionality. To accomplish this goal, the following syntax is proposed:

Level should be used for ALL situation that express a hierarchical position of text such as title, chapter, section, subsection, item, text, etc, etc, etc.  Jurisdictions vary widely on this and there is demonstrably no clear or satisfactorily achievable single formulation of these ambiguous and somewhat interchangeable words.  More to the point, determining the final use of each of these words is not needed to achieve the functional goal of expressing levels of text. 

Header is necessary and must be machinably expressed but can be an attribute of Level and does not require it's tag.

Text needs to be a tag.  Number however can be an attribute. 

# Example

`<Level Type = "Heading"> 17.10.1 Definitions </Level>`

to express the section numbers, for example, in the most elegant manner, it is included within the Level tag as another attribute, like this:

`<Level Num = "17.10.1">`

Alternative 1: When the Section of law includes text under the heading
`<Level Type = "Heading"> Definitions </Level>`
`<Level Text = "yes"> This law uses the following definitions </Level>`

Alternative 2: When the Section of law does not include text under the heading but instead continues directly to the next heading, which is therefore nested as a sub-section.

```<Level Type = "Heading"> Definitions </Level>
<Level Text = "no"> 

<Level Num = "17.10.1.1">
<Level Type = "Heading"> Dog </Level>
<Level Type = "Text"> "True"> A Dog is a K9 animal that we all love. </Level>```


It *might* be possible to further consolidate the tag and attribute set to one unified line, like this:

```<Level Num = "17.10.5.1" Heading = "yes" Text "no"> Dog </Level>
 A Dog is a K9 animal that we all love. </Level>```


Then, the only key piece of information missing is a unique identifier for each level of law.  This could be done by adding another attribute for the level to designate an id, like this:

```<Level Num = "17.10.5.1" Heading = "yes" Text "no" ID = "9876543210abcdefghijklmnop"> Dog </Level>
<Level Num = "17.10.5.1.1" Heading = "no" Text "yes" ID = "1234567890qwertyzxcvbnm"> A Dog is a K9 animal that we all love. </Level>```

Lastly, for the sake of achieving the most readable and understandable results, it may be best to use a convention whereby the tags are contained on their own line of no more than 100 characters so as to enable the entire tag to be displayed on one line only.  The content that is tagged should be contained on a separate line so that it can be read easily and distinguished from the machinable tags quickly.  Double spaces between all tag and content lines may be too much of a wasted space and Shreyash suggested  using double spaces only between levels for the best balance between readability and efficient use of space.  Here is an example: 

```<Level Num = "17.10.5.1" Heading = "yes" Text "no" ID = "9876543210abcdefghijklmnop"> 
Dog 
</Level>```

```<Level Num = "17.10.5.1.1" Heading = "no" Text "yes" ID = "1234567890qwertyzxcvbnm"> 
A Dog is a K9 animal that we all love. 
</Level>```
