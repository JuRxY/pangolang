#make your own functions like JOIN() that are not built in to pangolang
FUN JOIN(elements, seperator) 
	#variables are declared with VAR. Pangolang doesnt use types, so you can assign any type to a variable.
	VAR result = "" 
	#built in function LEN() returns the length of a string or array
	VAR len = LEN(elements)
	#Example of a FOR loop. "FOR i=0 TO len THEN" is the same as "for(i=0; i<len; i++)" in C
	FOR i=0 TO len THEN
		VAR result = result + elements/i
		IF i != len - 1 THEN VAR result = result + seperator
	END

	RETURN result
END

FUN drawRightHalfOfThePyramid()
	FOR i=0 TO 10 THEN
		#JOIN() is a function that takes an array and a seperator and returns a string with the elements of the array seperated by the seperator.
		PRINT(JOIN([(" "*1), ("*"*i)], ""))
	END
END

FUN drawLeftHalfOfThePyramid()
    VAR spaces = 10
	FOR i=0 TO 10 THEN
		PRINT(JOIN([(" "*spaces), ("*"*i)], ""))
        VAR spaces = spaces - 1
    END
END

FUN drawPyramidTiltedLeft()
	FOR i=0 TO 10 THEN
		PRINT(JOIN([(" "*i), ("*"*i)], ""))
	END
END

FUN drawPyramidTiltedRight()
	VAR spaces = 10
    FOR i=0 TO 10 THEN
        PRINT(JOIN([(" "*(10-i+spaces)), ("*"*i)], ""))
		VAR spaces = spaces - 1
    END
END

FUN drawCurveLeft()
	VAR spaces = 10
	FOR i=0 TO 10 THEN
		PRINT(JOIN([(" "*spaces * i), ("*"*i)], ""))
		VAR spaces = spaces - 1
	END
END



#calls all the declared pyramid functions
drawRightHalfOfThePyramid()
drawLeftHalfOfThePyramid()
drawPyramidTiltedLeft()
drawPyramidTiltedRight()
drawCurveLeft()