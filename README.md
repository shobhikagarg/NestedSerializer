# NestedSerializer
Django REST Api in nested serializers


Technologies --->
1. Django
2. Django-rest-framework (DRF)
3. REST APIs

Problem Description --->


• Create an API backend for an application with the following entity relation table given in
the Appendix. Use appropriate relational fields to relate Person to one of the City/
Town objects.
• Create APIs for Creation, reading, editing and deleting (CRUD) for all of the entities, with
the DRF’s APIView’s get, post, put, delete methods.
• Use DRF’s serialisers for all the CRUD operations.
• Create a CRUD API for Country with the ability to add nested data. i.e a dictionary of
Cities inside the states of the country. A single serialiser for the Country model should
be used for this API by modifying the create() and update() methods of
ModelSerializer from DRF. (hint: use nested serialisers)
• Add a SerializerMethodField() to the Country Serialiser to add a list of all the
states and cities in the country to a new custom field.
• Add people of the Person class to City and Town. Use an appropriate relational field.
• Create a Pagination API to list all the Persons in the database. With filtering based on
City, Town, State and Country. For each person return the related City, Town,
State and Country objects.
• For all API’s return DRF’s Response object with appropriate http status codes. Handle
cases of invalid data, duplicate entry for the same Country, State, City/Town object.
