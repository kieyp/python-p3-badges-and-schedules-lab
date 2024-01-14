def badge_maker(name):
    """Create a badge message for a given name."""
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    """Generate a list of badge messages for a list of names."""
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    """Assign rooms to a list of names and create a list of room assignment messages."""
    rooms = range(1, len(names) + 1)
    return [f"Hello, {name}! You'll be assigned to room {room}!" for name, room in zip(names, rooms)]

def printer(names):
    """Print badge messages and room assignment messages for a list of names."""
    badge_messages = batch_badge_creator(names)
    room_assignment_messages = assign_rooms(names)

    for badge_message in badge_messages:
        print(badge_message)

    for room_assignment_message in room_assignment_messages:
        print(room_assignment_message)

printer(names=['Arel', 'Carol'])
