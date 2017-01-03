"""
Utility to fill topics and topics_lookup collections based on some Google sheet we maintain
Both tables use strings as the Mongo unique id
Expected CSV Format (csv will have a header):
  Name | Primary lookup name | Synonym 1 | Synonym 2 | ...

topics {
  _id: name (primary key)
  formatted_name
}
topics_lookup {
  _id: synonym (primary key)
  topic
}
"""