# 奇异值分解

一张图片的数据信息是由像素（pixels）点阵组成的，一张彩色的图片即有三种颜色单元R,G,B的三个矩阵所决定。简单起见我们假设这三个矩阵都是方阵，维数$n \times n$。我们可以对$X_R,X_G,X_B$做SGD分解，得到
$$
X_R=U_R\Sigma_RV_R^T,\ X_G=U_G\Sigma_GV_G^T,\ X_B=U_B\Sigma_BV_B^T
$$
压缩的意思是指我们不存储全部的SVD信息，比如，对$X_R$来说，我们只存储的前k列（维数），记作$U_R^k$，只存储对角阵$Sigma_R$的前k个对角元组成的维数为的对角阵，记作$\Sigma_R^k$，只存储$V_R$的前k列，记作$V_R^k$。如此，在重构的时候，我们可以用一组比n低维的多的数据（k可以远小于n）来reconstruct ，同理我们也可以有降到k维的$X_G^k,X_B^k$。从本质来讲，如果假设原始的矩阵是满秩的，重构之后矩阵的秩（rank）从降到了。





```python
import numpy as np
import cv2

def SVD(pic, K):
    u_r, sigma_r, v_r = np.linalg.svd(pic[:, :, 0])
    u_g, sigma_g, v_g = np.linalg.svd(pic[:, :, 1])
    u_b, sigma_b, v_b = np.linalg.svd(pic[:, :, 2])

    def restore1(sigma,u,v,K):
        m = len(u)
        n = len(v[0])
        a = np.zeros((m, n))
        for k in range(K):
            uk = u[:, k].reshape(m, 1)
            vk = v[k].reshape(1, n)
            a += sigma[k] * np.dot(uk, vk)
        a[a < 0] = 0
        a[a > 255] = 255
        # a = a.clip(0, 255)
        return np.rint(a).astype('uint8')

    R = restore1(sigma_r, u_r, v_r, K)
    G = restore1(sigma_g, u_g, v_g, K)
    B = restore1(sigma_b, u_b, v_b, K)
    I = np.stack((R, G, B), 2)

    return I

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    K = int(sys.argv[2])
    pic = cv2.imread(path, flags=cv2.COLOR_BGR2RGB)
    I = SVD(pic, K)
    cv2.imshow("svd", I)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
```



sklearn实现：

```python
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
X = sparse_random_matrix(100, 100, density=0.01, random_state=42)
svd = TruncatedSVD(n_components=5, n_iter=7, random_state=42)
svd.fit(X)
TruncatedSVD(algorithm='randomized', n_components=5, n_iter=7, random_state=42, tol=0.0)
print(svd.explained_variance_ratio_)

print(svd.explained_variance_ratio_.sum())
```



作者：覃含章 链接：https://www.zhihu.com/question/34143886/answer/131046490
