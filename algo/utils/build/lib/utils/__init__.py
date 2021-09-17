
def g_convert(desc, matrix=False, directed=False):
  """
  TGF converter.
  """
  G = None
  vertices = 0
  phaze = 0
  for line in desc.strip().splitlines():
    if line == "#":
      if matrix:
        G = [[0] * vertices for _ in range(vertices)]
      else:
        G = [[] for i in range(vertices)]
      phaze = 1
      continue
    if phaze == 0:
      vertices += 1
    if phaze == 1:
      u, v, w = map(int, (line.split() + [1])[:3])
      if matrix:
        G[u][v] = w
        if not directed:
          G[v][u] = w
      else:
        G[u].append((v, w))
        if not directed:
          G[v].append((u, w))
  if not matrix:
    for v in range(vertices):
      G[v] = sorted(G[v])
  return G

class HeapItem:
  def __init__(self, priority: int, value: object):
    self.priority = priority
    self.value = value

  def __lt__(self, other):
    return self.priority < other.priority

  def __eq__(self, other):
    return self.priority == other.priority

class Heap:
  """
  Min-heap implementation.
  """
  def __init__(self):
    self._items = []

  def __len__(self):
    return len(self._items)

  @property
  def length(self):
    return len(self._items)

  @staticmethod
  def _left(i):
    return 2 * i + 1

  @staticmethod
  def _right(i):
    return 2 * i + 2

  @staticmethod
  def _parent(i):
    return (i - 1) // 2

  def _swap(self, i, j):
    self._items[i], self._items[j] = self._items[j], self._items[i]

  def _heapify(self, i):
    l = Heap._left(i)
    r = Heap._right(i)
    m = i

    if l < self.length and self._items[l] < self._items[m]:
      m = l
    if r < self.length and self._items[r] < self._items[m]:
      m = r

    if m != i:
      self._swap(m, i)
      self._heapify(m)

  def increase_priority(self, i, priority):
    if priority < self._items[i].priority:
      return
    self._items[i].priority = priority
    while i > 0 and self._items[Heap._parent(i)] > self._items[i]:
      self._swap(Heap._parent(i), i)
      i = Heap._parent(i)

  def top(self):
    return (self._items[0].priority, self._items[0].value) if self.length > 0 else None

  def get(self):
    if self.length == 0:
      return None
    self._swap(0, self.length - 1)
    item = self._items.pop()
    self._heapify(0)
    return (item.priority, item.value)

  def put(self, priority, value):
    self._items.append(HeapItem(float("-inf"), value))
    self.increase_priority(self.length - 1, priority)

class BSTNode:
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent
    self.lchild = None
    self.rchild = None

class BST:
  def __init__(self):
    self._root = None

  def __repr__(self):
    return self._print_tree(self._root)

  def _print_tree(self, node, level=0):
    result = ""
    if node != None:
      result += self._print_tree(node.rchild, level + 1)
      result += "{value: >{width}}\n".format(value=node.value, width=4*level)
      result += self._print_tree(node.lchild, level + 1)
    return result

  def find(self, value):
    curr = self._root
    while curr is not None and curr.value != value:
      if curr.value > value:
        curr = curr.lchild
      else:
        curr = curr.rchild
    return curr

  def _min(self, node):
    while node.lchild is not None:
      node = node.lchild
    return node

  def min(self):
    if self._root is None:
      return None
    return self._min(self._root)

  def _max(self, node):
    while node.rchild is not None:
      node = node.rchild
    return node

  def max(self):
    if self._root is None:
      return None
    return self._max(self._root)

  def insert(self, value):
    if self._root is None:
      self._root = BSTNode(value)
      return
    curr = self._root
    while True:
      if curr.value > value:
        if curr.lchild is None:
          curr.lchild = BSTNode(value, curr)
          break
        curr = curr.lchild
      else:
        if curr.rchild is None:
          curr.rchild = BSTNode(value, curr)
          break
        curr = curr.rchild

  def _transplant(self, u, v):
    if u.parent == None:
      self._root = v
    elif u == u.parent.lchild:
      u.parent.lchild = v
    else:
      u.parent.rchild = v
    if v != None:
      v.parent = u.parent

  def delete(self, value):
    z = self.find(value)
    if z is None:
      return

    if z.lchild is None:
      self._transplant(z, z.rchild)
    elif z.rchild is None:
      self._transplant(z, z.lchild)
    else:
      y = self._min(z.rchild)
      if y.parent != z:
        self._transplant(y, y.rchild)
        y.rchild = z.rchild
        y.rchild.parent = y
      self._transplant(z, y)
      y.lchild = z.lchild
      y.lchild.parent = y

  def successor(self, value):
    x = self.find(value)
    if x is None:
      return
    if x.rchild is not None:
      return self._min(x.rchild)
    y = x.parent
    while y is not None and x == y.rchild:
      x = y
      y = y.parent
    return y

  def predecessor(self, value):
    x = self.find(value)
    if x is None:
      return
    if x.lchild is not None:
      return self._max(x.lchild)
    y = x.parent
    while y is not None and x == y.lchild:
      x = y
      y = y.parent
    return y



from itertools import chain, zip_longest, repeat

JOINER_WIDTH = 1
DEFAULT_JOINER = ' ' * JOINER_WIDTH
CONNECTION_JOINER = '─' * JOINER_WIDTH
L_BRANCH_CONNECTOR = '─┘ '
LR_BRANCH_CONNECTOR = '─┴─'
R_BRANCH_CONNECTOR = ' └─'
L_NODE_CONNECTOR = '─┐ '
LR_NODE_CONNECTOR = '─┬─'
R_NODE_CONNECTOR= ' ┌─'


def multijoin(blocks, joiners=()):
    f"""
    Take one block (list of strings) or more and join them line by line with the specified joiners
    :param blocks: [['a', ...], ['b', ...], ...]
    :param joiners: ['─', ...]
    :return: ['a─b', ...]
    """

    # find maximum content width for each block
    block_content_width = tuple(max(map(len, block), default=0) for block in blocks)

    return tuple(

        joiner.join(

            (string or '')                 # string if present (see fillvalue below)
            .center(block_content_length)  # normalize content width across block

            for string, block_content_length in zip(block, block_content_width)

        )

        for block, joiner in zip(zip_longest(*blocks, fillvalue=None),
                                 chain(joiners, repeat(DEFAULT_JOINER))) # joiners or default

    )


def wire(block, connector):
    left_c = ' ' if connector == R_NODE_CONNECTOR else '─'
    right_c = ' ' if connector == L_NODE_CONNECTOR else '─'

    block, (left, right) = block

    if not (left or right):
        length = len(block[0])  # len of first line


        length -= 1             # ignore connector
        left = length // 2
        right = length - left

    return multijoin([[
        f'{left_c * left}{connector}{right_c * right}',
        *block
    ]])


def branch(blocks):
    wired_blocks = tuple(map(lambda blk: wire(blk, LR_NODE_CONNECTOR), blocks))
    return multijoin(wired_blocks, (CONNECTION_JOINER,))


def branch_left(blocks):
    last, *rest = blocks
    last = wire(last, R_NODE_CONNECTOR)
    rest = branch(rest)
    return multijoin([last, rest], (CONNECTION_JOINER,))


def branch_right(blocks):
    *rest, last = blocks
    rest = branch(rest)
    last = wire(last, L_NODE_CONNECTOR)
    return multijoin([rest, last], (CONNECTION_JOINER,))


def connect_branches(left, right):
    joiner = (LR_BRANCH_CONNECTOR if right else L_BRANCH_CONNECTOR) if left else R_BRANCH_CONNECTOR
    return multijoin([left, right], (joiner,))

def blocklen(block):
    if block:
        return len(block[0])
    else:
        return 0


def tree_print(current_node, left='lchild', right='rchild', nameattr='name'):
    if hasattr(current_node, nameattr):
        name = lambda node: getattr(node, nameattr)
    else:
        name = lambda node: str(node)

    children = lambda node: [getattr(node, left), getattr(node, right)] if node is not None else []
    nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1

    def balanced_branches(current_node):
        # size_branch = {child: nb_children(child) for child in children(current_node)}
        """ Creation of balanced lists for "a" branch and "b" branch. """
        # a = sorted(children(current_node), key=lambda node: nb_children(node))
        # b = []
        # while a and sum(size_branch[node] for node in b) < sum(size_branch[node] for node in a):
        #     b.append(a.pop())

        if len(children(current_node)) >= 2:
          a = [children(current_node)[0]]
          b = [children(current_node)[1]]
        else:
          a = []
          b = []
        return a, b

    print_tree_vertically(current_node, balanced_branches, name, children)


def tree_repr(current_node, balanced_branches, name, children):

    sx, dx = balanced_branches(current_node)

    """ Creation of children representation """

    tr_rpr = lambda node: tree_repr(node, balanced_branches, name, children)

    left = branch_left(map(tr_rpr, sx)) if sx else ()
    right = branch_right(map(tr_rpr, dx)) if dx else ()

    children_repr = tuple(
        connect_branches(
            left,
            right
        ) if sx or dx else ()
    )

    current_name = name(current_node)
    
    name_len = len(current_name)
    name_l, name_r = name_len // 2, name_len // 2

    left_len, right_len = blocklen(left), blocklen(right)
    
    current_name = f"{' ' * (left_len - name_l)}{current_name}{' ' * (right_len - name_r)}"

    return multijoin([[current_name, *children_repr]]), (max(left_len, name_l), max(right_len, name_r))


def print_tree_vertically(*args):
    print('\n'.join(tree_repr(*args)[0]))


def tree_print2(current_node, nameattr='value', left_child='lchild', right_child='rchild', indent='', last='updown'):

    if hasattr(current_node, nameattr):
        name = lambda node: getattr(node, nameattr)
    else:
        name = lambda node: str(node)

    up = getattr(current_node, right_child)
    down = getattr(current_node, left_child)

    if up is not None:
        next_last = 'up'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '|', ' ' * len(str(name(current_node))))
        tree_print2(up, nameattr, left_child, right_child, next_indent, next_last)

    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up is not None and down is not None: end_shape = '┤'
    elif up: end_shape = '┘'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node), end_shape))

    if down is not None:
        next_last = 'down'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '|', ' ' * len(str(name(current_node))))
        tree_print2(down, nameattr, left_child, right_child, next_indent, next_last)
