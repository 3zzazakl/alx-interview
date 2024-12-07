#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

def canUnlockAll(boxes):
	"""sumary_line
	
	Keyword arguments:
	argument -- description
	Return: return_description
	"""
	
	unlocked = set([0])
	
	to_process = list(unlocked)
	
	while to_process:
		current_box = to_process.pop()
		for key in boxes[current_box]:
			if key < len(boxes) and key not in unlocked:
				unlocked.add(key)
				to_process.append(key)
	
	return len(unlocked) == len(boxes)
