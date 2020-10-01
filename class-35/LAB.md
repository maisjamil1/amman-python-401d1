# Implementation: Graphs

## Specifications
- Read all of these instructions carefully. Name things exactly as described.
- Do all your work in a public repository (matching the example provided by your instructor) called `data-structures-and-algorithms`, with a well-formatted, detailed top-level README.md
- Create a branch in your repository called `graph`
- On your branch, create...
    - _C#_: a class library with a new class file named `Graph.cs`
    - _JavaScript_: a folder named `graph` which contains a file called `graph.js`
    - _Python_:a folder named `graph` which contains a file called `graph.py`
    - _Java_: a package named `graph` which contains a file called `Graph.java`
- Include any language-specific configuration files required for this challenge to become an individual component, module, library, etc.
    - _NOTE: You can find an example of this configuration for your course in your class lecture repository._

## Features
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

   1. AddNode()
        - Adds a new node to the graph
        - Takes in the value of that node
        - Returns the added node
   2. AddEdge()
       - Adds a new edge between two nodes in the graph
        - Include the ability to have a "weight"
        - Takes in the two nodes to be connected by the edge
            - Both nodes should already be in the Graph
   3. GetNodes()
      - Returns all of the nodes in the graph as a collection (set, list, or similar)
   4. GetNeighbors()
        - Returns a collection of edges connected to the given node
        - Takes in a given node
        - Include the weight of the connection in the returned collection
   5. Size()
      - Returns the total number of nodes in the graph


## Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:
1. Node can be successfully added to the graph
1. An edge can be successfully added to the graph
1. A collection of all nodes can be properly retrieved from the graph
1. All appropriate neighbors can be retrieved from the graph
1. Neighbors are returned with the weight between nodes included 
1. The proper size is returned, representing the number of nodes in the graph
1. A graph with only one node and edge can be properly returned
1. An empty graph properly returns null

Ensure your tests are passing before you submit your solution.

## Documentation: Your README.md

```markdown
# Graphs
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available in your Graph -->
```

## Submission Instructions
1. Create a pull request from your branch to your `master` branch
1. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents){:target="_blank"} of the specifications and tasks above, with the actual steps that you completed checked off
1. Submitting your completed work to Canvas:
    1. Copy the link to your open pull request and paste it into the corresponding Canvas assignment
    1. Leave a description of how long this assignment took you in the comments box
    1. Add any additional comments you like about your process or any difficulties you may have had with the assignment
1. Merge your branch into `master`, and delete your branch (don't worry, the PR link will still work)
