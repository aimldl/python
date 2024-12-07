* Rev.1: 2020-05-25 (Mon)
* Draft: 2018-10-28 (Sun)
# graphviz (Graph Visualization)
* [Graphviz](https://www.graphviz.org/) is open source graph visualization software.
* It is a way of representing structural information as diagrams of abstract graphs and networks.

## How to use it
Refer to [Quickstart](https://pypi.org/project/graphviz/).

## Appendix
```
graph1.gv

graph {
  a -- b;
  b --c;
  a--c;
  d--c;

}
```
Result

<img src="images/graphviz-graph1.png">
