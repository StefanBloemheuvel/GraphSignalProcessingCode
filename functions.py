def eigenvalues_vectors(graph, kind = 'A'):
    A = nx.adjacency_matrix(graph,nodelist=sorted(graph.nodes())).todense()
    D = np.diag(np.ravel(np.sum(A, axis=1)))
    L = D - A
    
    if kind == 'A':
        l, U = np.linalg.eigh(A) # hermitian or complex matrix

    if kind == 'L':
        l, U = np.linalg.eigh(L)

    return np.round(l, decimals=6), U

def method_2(graph):
    A = nx.adjacency_matrix(graph,nodelist=sorted(graph.nodes())).todense()
    D = np.diag(np.ravel(np.sum(A, axis=1)))
    L = D - A
    
    l, U = np.linalg.eig(L) # of a square array
    U = U[:,np.argsort(l)]
    l = l[np.argsort(l)]
    
    return np.round(l, 5), U

def method_3(graph):
    A = nx.adjacency_matrix(graph,nodelist=sorted(graph.nodes())).todense()
    D = np.diag(np.ravel(np.sum(A, axis=1)))
    L = D - A

    e = np.linalg.eigvals(L.A) # only eigenvalues
    e = np.linalg.eigvals(L)
    return np.round(e, decimals=6)

def method_4(graph):
    A = nx.adjacency_matrix(graph,nodelist=sorted(graph.nodes())).todense()
    D = np.diag(np.ravel(np.sum(A, axis=1)))
    L = D - A
    
    l, U = np.linalg.eigh(L)
    U = U[:,np.argsort(l)]
    l = l[np.argsort(l)]
    
    return np.round(l, 5), U
    
def check_symmetric(a, tol=1e-8):
    return np.all(np.abs(a-a.T) < tol)

def compute_gft(shift_matrix, graph_signal):
    eigenvalues, eigenvectors = np.linalg.eigh(shift_matrix)
    idx = eigenvalues.argsort()[::-1]
    sorted_eigenvalues = eigenvalues[idx]
    sorted_eigenvectors = eigenvectors[:, idx]
    return np.dot(eigenvectors.T.conj(), graph_signal)


