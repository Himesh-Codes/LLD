from hackathon import HackathonPlatform

class HackathonTest():
    platform = HackathonPlatform()
    user_id_1 = None
    user_id_2 = None

    def testAddProblems(self):
        # Add problems
        self.platform.add_problem("Description 1", "tag1", "easy", 10)
        self.platform.add_problem("Description 2", "tag2", "medium", 20)
        self.platform.add_problem("Description 3", "tag1", "hard", 30)

    def testAddUsers(self):
        # Add users
        self.user_id_1 = self.platform.add_user("Alice", "Engineering")
        self.user_id_2 = self.platform.add_user("Bob", "Marketing")
        print(self.user_id_1)
        print(self.user_id_2)

    def testFetchProblems(self):
        # Fetch problems
        print("----filtering easy probs------")
        print(self.platform.fetch_problems(difficulty="easy"))
        print("----filtering tag1 probs------")
        print(self.platform.fetch_problems(tag="tag1"))
        print("----sorting on scores of probs------")
        print(self.platform.fetch_problems(sort_by="score"))
    
    def testSolveProblems(self):
        # Solve problems
        try:
            self.platform.solve_problem(self.user_id_1, 1, 5.0)
            self.platform.solve_problem(self.user_id_2, 2, 15.0)
        except ValueError as e:
            print(f"Error: {e}")
        
        print("successfully solved probs")

    def testFetchSolveProblems(self):
        # Fetch solved problems
        try:
            print(self.platform.fetch_solved_problems(self.user_id_1))
        except ValueError as e:
            print(f"Error: {e}")
    
    def testGetLeader(self):
        # Get leader
        try:
            print(self.platform.get_leader())
        except ValueError as e:
            print(f"Error: {e}")
    
    def testProblemStat(self):
            # Extension: Problem stats
        try:
            print(self.platform.problem_stats(1))
            print(self.platform.problem_stats(2))
            # invalid prob id testcase
            print(self.platform.problem_stats(7))
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    
    test = HackathonTest()
    print("------------test case start-------")
    test.testAddProblems()
    print("------------test case end-------")
    print("------------test case start-------")
    test.testAddUsers()
    print("------------test case end-------")
    print("------------test case start-------")
    test.testFetchProblems()
    print("------------test case end-------")
    print("------------test case start-------")
    test.testSolveProblems()
    print("------------test case end-------")
    print("------------test case start-------")
    test.testFetchSolveProblems()
    print("------------test case end-------")
    print("------------test case start-------")
    test.testGetLeader()
    print("------------test case end-------")
    print("------------test case start-------")
    test.testProblemStat()
    print("------------test case end-------")


    

    

    

    

    

