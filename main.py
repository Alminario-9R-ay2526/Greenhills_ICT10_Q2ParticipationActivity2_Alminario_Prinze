from js import document
from pyscript import display

# Predefine at least four sets representing existing members across grade levels
grade_7 = {"Alice Blue", "Anita Bath", "Billy Sparks"}
grade_8 = {"Eileen Dover", "Elia Vator", "Francisco Portero"}
grade_9 = {"Joe Kern", "Juanito Lakarin", "Justin Case", "Ligaya Anonuevo"}
grade_10 = {"Paige Turne", "Restituto Fruto", "Sheldon Cooper", "Ram Nguyen"}

# Combine the predefined grade sets using the set union operator (|)
base_members = grade_7 | grade_8 | grade_9 | grade_10


def get_name(event=None):
    # Retrieve the input element and user input value using js.document
    input_element = document.getElementById("name")
    input_name = input_element.value

    # Create a single-element set with the newly entered name
    new_member_set = {input_name}

    # Combine existing members and the new member set using the set union operator (|)
    master_set = base_members | new_member_set

    # Convert the set into a sorted list for consistent alphabetical output
    sorted_members = sorted(master_set)

    # Format list into HTML line breaks using string joining
    members_list_html = "<br>".join(sorted_members)

    # Calculate total count of members using len()
    total_count = len(master_set)

    # Construct complete HTML output string using f-strings
    output_html = f"<strong>All members</strong><br>{members_list_html}<br><br><strong>Total members: {total_count}</strong>"

    # Target the output container div and render HTML content directly
    output_div = document.getElementById("output")
    output_div.innerHTML = output_html