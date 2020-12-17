#! /usr/bin/python3
"""
Community Party

You are hosting a party, and people keep arriving in pairs. You want to know how everyone knows
one another, so people with no common communities can get to know one another. The pairs are 
defined as couples with names, ie ("Matt", "Sabrina"). Can you be the party matcher?
"""

# Store all the communities in a single list. Each community is its own list inside
# 	this main list. 
communities = []

def search_for(left, right):
	"""
	Search for which communities two people belong to.
	O(N) worst case where N is the number of people at the party.
	"""
	left_community = None
	right_community = None
	for community_index in range(len(communities)):
		for value in communities[community_index]:
			if left == value:
				left_community = community_index
				if left_community is not None and right_community is not None:
					break
			elif right == value:
				right_community = community_index
				if left_community is not None and right_community is not None:
					break
	return left_community, right_community

def add(pair):
	"""
	A new couple walks in the door! Add them to the communities they belong to.
	Insertion requires finding the current communities for the couple, and adding them
	if needed. O(N) for search + O(N) for insertion where N is the number of people at
	the party.
	"""
	# Get the communities the individuals belong to.
	left = pair[0]
	right = pair[1]
	left_community, right_community = search_for(left, right)

	if left_community is not None and right_community is not None and left_community != right_community:
		# both being not none (add both together)
		communities[left_community] = communities[left_community] + communities[right_community]
		communities.pop(right_community)
	elif left_community is not None and right_community is None:
		# right being none and left being something (add to left)
		communities[left_community].append(right)
	elif right_community is not None and left_community is None:
		# left being none and right being something (add left to right)
		communities[right_community].append(left)
	elif left_community is None and right_community is None:
		# Check for both being none (add new community with them)
		communities.append([left, right])
	# elif left_community is not None and right_community is not None and left_community == right_community  # Do nothing

def search(pair):
	"""
	Find out if one person is in the same community as another.
	O(N) using search_for.
	@return Whether the pair is from the same community
	"""
	# Get the communities the individuals belong to.
	left = pair[0]
	right = pair[1]
	left_community, right_community = search_for(left, right)

	# If they are from the same community return true
	if left_community == right_community:
		return True
	return False

if __name__ == "__main__":
	# A bunch of people come to the party
	add(("A", "B"))
	add(("B", "C"))
	add(("A", "D"))
	add(("B", "C"))
	add(("X", "Y"))
	add(("G", "F"))
	add(("A", "F"))

	# Find out if someone is not included
	assert search(("A", "B")) == True
	assert search(("A", "F")) == True
	assert search(("A", "G")) == True
	assert search(("X", "F")) == False

	# Found out how many communities are at the party
	assert len(communities) == 2  # O(N) where N is the number of communities


