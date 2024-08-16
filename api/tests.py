from django.test import TestCase
from graphene.test import Client
from api.schema import schema
from api.models import Bank, Branch

class BankBranchQueryTest(TestCase):

    def setUp(self):
        self.client = Client(schema)
        # Create a Bank
        self.bank = Bank.objects.create(name="Axis")
        # Create a Branch associated with the Bank
        self.branch = Branch.objects.create(
            ifsc="AXIS1234567",
            bank=self.bank,
            branch_name="Main Branch",
            address="123 Main St",
            city="Cityville",
            district="District X",
            state="State Y"
        )

    def test_query_branches(self):
        query = '''
        query {
            branches {
                ifsc
                branchName
                address
                city
                district
                state
                bank {
                    name
                }
            }
        }
        '''
        # Execute the query
        response = self.client.execute(query)
        
        # Assert no errors
        self.assertIsNone(response.errors)

        # Get data from response
        data = response.data['branches'][0]

        # Validate the returned data
        self.assertEqual(data['ifsc'], "AXIS1234567")
        self.assertEqual(data['branchName'], "Main Branch")
        self.assertEqual(data['bank']['name'], "Axis")
        self.assertEqual(data['city'], "Cityville")
