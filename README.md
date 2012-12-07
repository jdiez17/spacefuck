Spacefuck
=========

Spacefuck is a [Turing complete](http://en.wikipedia.org/wiki/Turing_completeness) [esoteric programming language](http://en.wikipedia.org/wiki/Esoteric_programming_language) based on Brainfuck. It also takes inspiration from the [Whitespace programming language](http://en.wikipedia.org/wiki/Whitespace_(programming_language)).
The commands are those of Brainfuck, but instead of using single characters, Spacefuck uses a line for each command. 

The number of characters per line represents the action that the Spacefuck interpreter will perform. 

Why?
----

I was bored, and my Internet connection was not working. I also wanted to experiment with esoteric languages. What makes this one interesting, though, is that you can write text in your program. This means that programs can be self-descripting. A good example of this is *hello.sf*. There are a couple of test programs that you can find in the *examples* folder. Feel free to submit your own Spacefuck program!

Commands
--------

<table>
	<tr>
		<th>Characters per line</th>
		<th>Brainfuck equivalent</th>
		<th>Effect</th>
	</tr>
	<tr>
		<td>1</td>
		<td>></td>
		<td>Increments the pointer by one.</td>
	</tr>
	<tr>
		<td>2</td>
		<td><</td>
		<td>Decrements the pointer by one.</td>
	</tr>
	<tr>
		<td>3</td>
		<td>+</td>
		<td>Increments the value of memory at the pointer.</td>
	</tr>
	<tr>
		<td>4</td>
		<td>-</td>
		<td>Decrements the value of memory at the pointer.</td>
	</tr>
	<tr>
		<td>5</td>
		<td>.</td>
		<td>Outputs the value of memory at the pointer (encoded as ASCII)</td>
	</tr>
	<tr>
		<td>6</td>
		<td>,</td>
		<td>Gets one byte of input from the input stream and stores it.</td>
	</tr>
	<tr>
		<td>7</td>
		<td>[</td>
		<td>Checks if the memory value at the pointer equals zero. If it does, the interpreter will jump **forward** to the command after the matching *8* command.</td>
	</tr>
	<tr>
		<td>8</td>
		<td>]</td>
		<td>Checks if the memory value at the pointer is different from zero. If it does, the intepreter will jump **back** to the command after the matching *7* command.</td>
	</tr>
</td>
