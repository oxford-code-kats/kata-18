import unittest
from dependencies import Tracker

class TestDependencies(unittest.TestCase):

    def test_basic(self):
        tracker = Tracker()
        tracker.add_direct('A', ['B', 'C'] )
        tracker.add_direct('B', ['C', 'E'] )
        tracker.add_direct('C', ['G' ] )
        tracker.add_direct('D', ['A', 'F'])
        tracker.add_direct('E', ['F'] )
        tracker.add_direct('F',  ['H'] )

        self.assertEqual( [ 'B', 'C', 'E', 'F', 'G', 'H' ],   tracker.dependencies_for('A'))
        self.assertEqual( [ 'C', 'E', 'F', 'G', 'H' ],     tracker.dependencies_for('B'))
        self.assertEqual( [ 'G' ],             tracker.dependencies_for('C'))
        self.assertEqual( [ 'A', 'B', 'C', 'E', 'F', 'G', 'H' ], tracker.dependencies_for('D'))
        self.assertEqual( [ 'F', 'H' ],           tracker.dependencies_for('E'))
        self.assertEqual( [ 'H' ],             tracker.dependencies_for('F'))

    def test_cyclic_deps(self):
        tracker = Tracker()
        tracker.add_direct('A', ['B'])
        tracker.add_direct('B', ['C'])
        tracker.add_direct('C', ['A'])

        self.assertEqual(['B', 'C'],   tracker.dependencies_for('A'))


if __name__ == '__main__':
    unittest.main()