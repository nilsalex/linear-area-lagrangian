from cadabra2 import *

Indices(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''fourD, position=independent''') )
Integer(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''0..4''') )

Indices(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''threeD, position=independent, parent=fourD''') )
Integer(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''1..3''') )

KroneckerDelta(Ex(r'''\delta{#}'''), Ex(r'''''') )
Symmetric(Ex(r'''\gamma_{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''\gamma^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''X^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''Y^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''Z^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''U^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''dU^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''V^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''dV^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''W^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''dW^{\alpha \beta}'''), Ex(r'''''') )
EpsilonTensor(Ex(r'''\epsilon_{\alpha \beta \gamma}'''), Ex(r'''''') )
EpsilonTensor(Ex(r'''\epsilon^{\alpha \beta \gamma}'''), Ex(r'''''') )

Symmetric(Ex(r'''\eta_{a? b?}'''), Ex(r'''''') )
AntiSymmetric(Ex(r'''\epsilon_{a? b? c? d?}'''), Ex(r'''''') )

PartialDerivative(Ex(r'''\partial{#}'''), Ex(r''')''') )
Depends(Ex(r'''H{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''H1{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''H2{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''H3{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''X{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''Y{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''Z{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''U{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dU{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''V{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dV{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''W{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dW{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''B{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dB{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''A'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dA'''), Ex(r'''\partial{#})''') )

SortOrder(Ex(r'''{dU{#},dV{#},dW{#},dB{#},dA,m{#},k{#},t{#},e{#},A,B{#},X{#},Y{#},Z{#},U{#},V{#},W{#},\partial{#},\epsilon{#},\gamma{#}}'''), Ex(r''')''') )

ruleH1  = Ex(r''' H1_{\mu \nu} -> X_{\mu \nu}''')
ruleH2  = Ex(r''' H2_{\mu \nu \rho} -> \epsilon_{\alpha \nu \rho} * \gamma^{\alpha \sigma} Z_{\mu \sigma}''')
ruleH3  = Ex(r''' H3_{\mu \nu \rho \sigma} -> \epsilon_{\alpha \mu \nu} \epsilon_{\beta \rho \sigma} \gamma^{\alpha \gamma} \gamma^{\beta \delta} Y_{\gamma \delta}''')

ruleEta001  = Ex(r''' \eta_{0 0} -> 1''')
ruleEta002  = Ex(r''' \eta^{0 0} -> 1''')
ruleEta0a11  = Ex(r''' \eta_{0 \alpha} -> 0''')
ruleEta0a21  = Ex(r''' \eta_{\alpha 0} -> 0''')
ruleEta0a12  = Ex(r''' \eta^{0 \alpha} -> 0''')
ruleEta0a22  = Ex(r''' \eta^{\alpha 0} -> 0''')
ruleEtaab1  = Ex(r''' \eta^{\alpha \beta} -> -\gamma^{\alpha \beta}''')
ruleEtaab2  = Ex(r''' \eta_{\alpha \beta} -> -\gamma_{\alpha \beta}''')

ruleEtaEta1 = Ex(r'''\eta^{a? p} \eta_{b? p} -> \delta^{a?}_{b?}''')
ruleEtaEta2 = Ex(r'''\eta^{a? p} \eta_{p b?} -> \delta^{a?}_{b?}''')
ruleEtaEta3 = Ex(r'''\eta^{p a?} \eta_{b? p} -> \delta^{a?}_{b?}''')
ruleEtaEta4 = Ex(r'''\eta^{p a?} \eta_{p b?} -> \delta^{a?}_{b?}''')

ruleEtaEpsilon1 = Ex(r'''\eta^{a? p} \epsilon_{p \alpha \beta \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon2 = Ex(r'''\eta^{p a?} \epsilon_{p \alpha \beta \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon3 = Ex(r'''\eta^{a? p} \epsilon_{\alpha p \beta \gamma} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon4 = Ex(r'''\eta^{p a?} \epsilon_{\alpha p \beta \gamma} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon5 = Ex(r'''\eta^{a? p} \epsilon_{\alpha \beta p \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon6 = Ex(r'''\eta^{p a?} \epsilon_{\alpha \beta p \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon7 = Ex(r'''\eta^{a? p} \epsilon_{\alpha \beta \gamma p} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon8 = Ex(r'''\eta^{p a?} \epsilon_{\alpha \beta \gamma p} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')

ruleDelta1 = Ex(r'''\delta_{p?}^{q?} -> \delta^{q?}_{p?}''')
ruleDelta2 = Ex(r'''\delta^{0}_{\alpha} -> 0''')
ruleDelta3 = Ex(r'''\delta^{\alpha}_{0} -> 0''')

ruleDeltaDelta1 = Ex(r'''\delta^{p}_{q?} \delta^{r?}_{p} -> \delta^{r?}_{q?}''')
ruleDeltaDelta2 = Ex(r'''\delta^{r?}_{p} \delta^{p}_{q?} -> \delta^{r?}_{q?}''')

ruleTraceFree1  = Ex(r''' \gamma_{\alpha \beta} W^{\alpha \beta} -> 0''')
ruleTraceFree2  = Ex(r''' \gamma_{\alpha \beta} \partial_{p?}{W^{\alpha \beta}} -> 0''')
ruleTraceFree3  = Ex(r''' \gamma_{\alpha \beta} \partial_{p? q?}{W^{\alpha \beta}} -> 0''')

ruleX  = Ex(r''' X^{\alpha \beta} -> (1/2) * (U^{\alpha \beta} + V^{\alpha \beta})''')
ruleY  = Ex(r''' Y^{\alpha \beta} -> (-1/2) * (U^{\alpha \beta} - V^{\alpha \beta})''')
ruleZ  = Ex(r''' Z^{\alpha \beta} -> (1/2) * W^{\alpha \beta}''')

ruleEps0000  = Ex(r''' \epsilon_{0 0 0 0} -> 0''')
ruleEps000a1  = Ex(r''' \epsilon_{0 0 0 \alpha} -> 0''')
ruleEps000a2  = Ex(r''' \epsilon_{0 0 \alpha 0} -> 0''')
ruleEps000a3  = Ex(r''' \epsilon_{0 \alpha 0 0} -> 0''')
ruleEps000a4  = Ex(r''' \epsilon_{\alpha 0 0 0} -> 0''')
ruleEps00ab1  = Ex(r''' \epsilon_{0 0 \alpha \beta} -> 0''')
ruleEps00ab2  = Ex(r''' \epsilon_{0 \alpha 0 \beta} -> 0''')
ruleEps00ab3  = Ex(r''' \epsilon_{0 \alpha \beta 0} -> 0''')
ruleEps00ab4  = Ex(r''' \epsilon_{\alpha 0 0 \beta} -> 0''')
ruleEps00ab5  = Ex(r''' \epsilon_{\alpha 0 \beta 0} -> 0''')
ruleEps00ab6  = Ex(r''' \epsilon_{\alpha \beta 0 0} -> 0''')
ruleEps0abc1  = Ex(r''' \epsilon_{0 \alpha \beta \gamma} -> \epsilon_{\alpha \beta \gamma}''')
ruleEps0abc2  = Ex(r''' \epsilon_{\alpha 0 \beta \gamma} -> -\epsilon_{\alpha \beta \gamma}''')
ruleEps0abc3  = Ex(r''' \epsilon_{\alpha \beta 0 \gamma} -> \epsilon_{\alpha \beta \gamma}''')
ruleEps0abc4  = Ex(r''' \epsilon_{\alpha \beta \gamma 0} -> -\epsilon_{\alpha \beta \gamma}''')
ruleEpsabcd  = Ex(r''' \epsilon_{\alpha \beta \gamma \delta} -> 0''')

rulegg1  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \nu} -> 3''')
rulegg2  = Ex(r''' \gamma^{\mu \nu} \gamma_{\nu \mu} -> 3''')
rulegg3  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg4  = Ex(r''' \gamma^{\mu \nu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')
rulegg5  = Ex(r''' \gamma^{\nu \mu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg6  = Ex(r''' \gamma^{\nu \mu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')

ruleEpsToDelta1  = Ex(r''' \epsilon_{a? b? c?} \epsilon_{i? j? k?} ->\gamma_{a? i?} \gamma_{b? j?} \gamma_{c? k?} - \gamma_{a? i?} \gamma_{b? k?} \gamma_{c? j?} - \gamma_{a? j?} \gamma_{b? i?} \gamma_{c? k?} + \gamma_{a? j?} \gamma_{b? k?} \gamma_{c? i?} + \gamma_{a? k?} \gamma_{b? i?} \gamma_{c? j?} - \gamma_{a? k?} \gamma_{b? j?} \gamma_{c? i?}''')

ruleEpsToDelta2  = Ex(r''' \epsilon^{a? b? c?} \epsilon^{i? j? k?} ->\gamma^{a? i?} \gamma^{b? j?} \gamma^{c? k?} - \gamma^{a? i?} \gamma^{b? k?} \gamma^{c? j?} - \gamma^{a? j?} \gamma^{b? i?} \gamma^{c? k?} + \gamma^{a? j?} \gamma^{b? k?} \gamma^{c? i?} + \gamma^{a? k?} \gamma^{b? i?} \gamma^{c? j?} - \gamma^{a? k?} \gamma^{b? j?} \gamma^{c? i?}''')

ruleEpsToDelta3  = Ex(r''' \epsilon^{a? b? c?} \epsilon_{i? j? k?} ->\delta^{a?}_{i?} \delta^{b?}_{j?} \delta^{c?}_{k?} - \delta^{a?}_{i?} \delta^{b?}_{k?} \delta^{c?}_{j?} - \delta^{a?}_{j?} \delta^{b?}_{i?} \delta^{c?}_{k?} + \delta^{a?}_{j?} \delta^{b?}_{k?} \delta^{c?}_{i?} + \delta^{a?}_{k?} \delta^{b?}_{i?} \delta^{c?}_{j?} - \delta^{a?}_{k?} \delta^{b?}_{j?} \delta^{c?}_{i?}''')

allE = Ex(r'''e{1}, e{2}, e{3}, e{4}, e{5}, e{6}, e{7}, e{8}, e{9}, e{10}, e{11}, e{12}, e{13}, e{14}, e{15}, e{16}, e{17}, e{18}, e{19}, e{20}, e{21}, e{22}, e{23}, e{24}, e{25}, e{26}, e{27}, e{28}, e{29}, e{30}, e{31}, e{32}, e{33}, e{34}, e{35}, e{36}, e{37}, e{38}, e{39}, e{40}''')

def my_eliminate_metric(ex, repeat=False):
    substitute(ex, Ex(r'''\delta_{\alpha \beta} -> \gamma_{\alpha \beta}''', False), repeat=repeat)
    substitute(ex, Ex(r'''\delta^{\alpha \beta} -> \gamma^{\alpha \beta}''', False), repeat=repeat)
    substitute(ex, rulegg1, repeat=repeat)
    substitute(ex, rulegg2, repeat=repeat)
    substitute(ex, rulegg3, repeat=repeat)
    substitute(ex, rulegg4, repeat=repeat)
    substitute(ex, rulegg5, repeat=repeat)
    substitute(ex, rulegg6, repeat=repeat)
    return ex

def my_epsilon_to_delta(ex, repeat=False):
    substitute(ex, ruleEpsToDelta3)
    substitute(ex, ruleEpsToDelta1)
    substitute(ex, ruleEpsToDelta2)
    return ex

def kin_ABI():
    ruleM1  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? j?}''')
    ruleM2  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? j?}''')
    ruleM3  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? e?} \eta_{d? g?} \eta_{f? h?} \eta_{i? j?}''')
    ruleM4  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? e?} \eta_{d? g?} \eta_{f? i?} \eta_{h? j?}''')
    ruleM5  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? e?} \eta_{d? i?} \eta_{f? g?} \eta_{h? j?}''')
    ruleM6  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? i?} \eta_{d? j?} \eta_{e? g?} \eta_{f? h?}''')
    ruleM7  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? e?} \eta^{b? f?} \eta_{c? g?} \eta_{d? h?} \eta_{i? j?}''')
    ruleM8  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? e?} \eta^{b? f?} \eta_{c? g?} \eta_{d? i?} \eta_{h? j?}''')
    ruleM9  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? e?} \eta^{b? g?} \eta_{c? f?} \eta_{d? h?} \eta_{i? j?}''')
    ruleM10 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? c? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? j?}''')
    ruleM11 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? c? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? j?}''')
    ruleM12 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? e? f?} \eta_{c? g?} \eta_{d? h?} \eta_{i? j?}''')
    ruleM13 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? e? f?} \eta_{c? g?} \eta_{d? i?} \eta_{h? j?}''')
    ruleM14 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? e? i?} \eta_{c? f?} \eta_{d? g?} \eta_{h? j?}''')
    ruleM15 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? e? i?} \eta_{c? g?} \eta_{d? h?} \eta_{f? j?}''')
    ruleM16 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{e? f? g? h?} \eta_{a? c?} \eta_{b? d?} \eta_{i? j?}''')
    
    ruleM  = Ex(r''' M^{a? b? c? d? e? f? g? h? i? j?} ->e{1} * M{1}^{a? b? c? d? e? f? g? h? i? j?} + e{2} * M{2}^{a? b? c? d? e? f? g? h? i? j?} + e{3} * M{3}^{a? b? c? d? e? f? g? h? i? j?} + e{4} * M{4}^{a? b? c? d? e? f? g? h? i? j?} + e{5} * M{5}^{a? b? c? d? e? f? g? h? i? j?} + e{6} * M{6}^{a? b? c? d? e? f? g? h? i? j?} + e{7} * M{7}^{a? b? c? d? e? f? g? h? i? j?} + e{8} * M{8}^{a? b? c? d? e? f? g? h? i? j?} + e{9} * M{9}^{a? b? c? d? e? f? g? h? i? j?} + e{10} * M{10}^{a? b? c? d? e? f? g? h? i? j?} + e{11} * M{11}^{a? b? c? d? e? f? g? h? i? j?} + e{12} * M{12}^{a? b? c? d? e? f? g? h? i? j?} + e{13} * M{13}^{a? b? c? d? e? f? g? h? i? j?} + e{14} * M{14}^{a? b? c? d? e? f? g? h? i? j?} + e{15} * M{15}^{a? b? c? d? e? f? g? h? i? j?} + e{16} * M{16}^{a? b? c? d? e? f? g? h? i? j?}''')
    
    ruleMH1  = Ex(r''' M^{a b c d e? f? g? h? i? j?} H_{a b c d} ->(M^{0 \mu 0 \nu e? f? g? h? i? j?} - M^{0 \mu \nu 0 e? f? g? h? i? j?} - M^{\mu 0 0 \nu e? f? g? h? i? j?} + M^{\mu 0 \nu 0 e? f? g? h? i? j?}) H1_{\mu \nu} + (M^{0 \mu \nu \rho e? f? g? h? i? j?} - M^{\mu 0 \nu \rho e? f? g? h? i? j?} + M^{\nu \rho 0 \mu e? f? g? h? i? j?} - M^{\nu \rho \mu 0 e? f? g? h? i? j?}) H2_{\mu \nu \rho} + M^{\mu \nu \rho \sigma e? f? g? h? i? j?} H3_{\mu \nu \rho \sigma}''')
    
    ruleMH2  = Ex(r''' M^{e? f? g? h? a b c d p q} \partial_{p q}{H_{a b c d}} ->(M^{e? f? g? h? 0 \mu 0 \nu 0 0} - M^{e? f? g? h? 0 \mu \nu 0 0 0} - M^{e? f? g? h? \mu 0 0 \nu 0 0} + M^{e? f? g? h? \mu 0 \nu 0 0 0}) \partial_{0 0}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu 0 \nu 0 \alpha} - M^{e? f? g? h? 0 \mu \nu 0 0 \alpha} - M^{e? f? g? h? \mu 0 0 \nu 0 \alpha} + M^{e? f? g? h? \mu 0 \nu 0 0 \alpha}) \partial_{0 \alpha}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu 0 \nu \alpha 0} - M^{e? f? g? h? 0 \mu \nu 0 \alpha 0} - M^{e? f? g? h? \mu 0 0 \nu \alpha 0} + M^{e? f? g? h? \mu 0 \nu 0 \alpha 0}) \partial_{0 \alpha}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu 0 \nu \alpha \beta} - M^{e? f? g? h? 0 \mu \nu 0 \alpha \beta} - M^{e? f? g? h? \mu 0 0 \nu \alpha \beta} + M^{e? f? g? h? \mu 0 \nu 0 \alpha \beta}) \partial_{\alpha \beta}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu \nu \rho 0 0} - M^{e? f? g? h? \mu 0 \nu \rho 0 0} + M^{e? f? g? h? \nu \rho 0 \mu 0 0} - M^{e? f? g? h? \nu \rho \mu 0 0 0}) \partial_{0 0}{H2_{\mu \nu \rho}} + (M^{e? f? g? h? 0 \mu \nu \rho 0 \alpha} - M^{e? f? g? h? \mu 0 \nu \rho 0 \alpha} + M^{e? f? g? h? \nu \rho 0 \mu 0 \alpha} - M^{e? f? g? h? \nu \rho \mu 0 0 \alpha}) \partial_{0 \alpha}{H2_{\mu \nu \rho}} + (M^{e? f? g? h? 0 \mu \nu \rho \alpha 0} - M^{e? f? g? h? \mu 0 \nu \rho \alpha 0} + M^{e? f? g? h? \nu \rho 0 \mu \alpha 0} - M^{e? f? g? h? \nu \rho \mu 0 \alpha 0}) \partial_{0 \alpha}{H2_{\mu \nu \rho}} + (M^{e? f? g? h? 0 \mu \nu \rho \alpha \beta} - M^{e? f? g? h? \mu 0 \nu \rho \alpha \beta} + M^{e? f? g? h? \nu \rho 0 \mu \alpha \beta} - M^{e? f? g? h? \nu \rho \mu 0 \alpha \beta}) \partial_{\alpha \beta}{H2_{\mu \nu \rho}} + M^{e? f? g? h? \mu \nu \rho \sigma 0 0} \partial_{0 0}{H3_{\mu \nu \rho \sigma}} + M^{e? f? g? h? \mu \nu \rho \sigma 0 \alpha} \partial_{0 \alpha}{H3_{\mu \nu \rho \sigma}} + M^{e? f? g? h? \mu \nu \rho \sigma \alpha 0} \partial_{0 \alpha}{H3_{\mu \nu \rho \sigma}} + M^{e? f? g? h? \mu \nu \rho \sigma \alpha \beta} \partial_{\alpha \beta}{H3_{\mu \nu \rho \sigma}}''')
    
    ex  = Ex(r'''M^{a b c d e f g h i j} H_{a b c d} \partial_{i j}{H_{e f g h}}''')
    
    
    substitute(ex, ruleMH1)
    distribute(ex)
    substitute(ex, ruleMH2)
    distribute(ex)
    
    
    substitute(ex, ruleM)
    substitute(ex, ruleM1)
    substitute(ex, ruleM2)
    substitute(ex, ruleM3)
    substitute(ex, ruleM4)
    substitute(ex, ruleM5)
    substitute(ex, ruleM6)
    substitute(ex, ruleM7)
    substitute(ex, ruleM8)
    substitute(ex, ruleM9)
    substitute(ex, ruleM10)
    substitute(ex, ruleM11)
    substitute(ex, ruleM12)
    substitute(ex, ruleM13)
    substitute(ex, ruleM14)
    substitute(ex, ruleM15)
    substitute(ex, ruleM16)

    three_plus_one(ex)

    return(ex)

def eliminate_eta(ex):
    substitute(ex, ruleEtaEta1, repeat=True)
    substitute(ex, ruleEtaEta2, repeat=True)
    substitute(ex, ruleEtaEta3, repeat=True)
    substitute(ex, ruleEtaEta4, repeat=True)

def three_plus_one_eta(ex):
    substitute(ex, ruleEta001, repeat=True)
    substitute(ex, ruleEta0a11, repeat=True)
    substitute(ex, ruleEta0a21, repeat=True)
    substitute(ex, ruleEtaab1, repeat=True)
    
    substitute(ex, ruleEta002, repeat=True)
    substitute(ex, ruleEta0a12, repeat=True)
    substitute(ex, ruleEta0a22, repeat=True)
    substitute(ex, ruleEtaab2, repeat=True)

def my_eliminate_kronecker(ex):
    substitute(ex, ruleDeltaDelta1, repeat=True)
    substitute(ex, ruleDeltaDelta2, repeat=True)

def three_plus_one_delta(ex):
    substitute(ex, ruleDelta2, repeat=True)
    substitute(ex, ruleDelta3, repeat=True)

def three_plus_one_epsilon(ex):
    substitute(ex, ruleEps0000, repeat=True)
    substitute(ex, ruleEps000a1, repeat=True)
    substitute(ex, ruleEps000a2, repeat=True)
    substitute(ex, ruleEps000a3, repeat=True)
    substitute(ex, ruleEps000a4, repeat=True)
    substitute(ex, ruleEps00ab1, repeat=True)
    substitute(ex, ruleEps00ab2, repeat=True)
    substitute(ex, ruleEps00ab3, repeat=True)
    substitute(ex, ruleEps00ab4, repeat=True)
    substitute(ex, ruleEps00ab5, repeat=True)
    substitute(ex, ruleEps00ab6, repeat=True)
    substitute(ex, ruleEps0abc1, repeat=True)
    substitute(ex, ruleEps0abc2, repeat=True)
    substitute(ex, ruleEps0abc3, repeat=True)
    substitute(ex, ruleEps0abc4, repeat=True)
    substitute(ex, ruleEpsabcd, repeat=True)

def subs_delta_eta(ex):
    substitute(ex, Ex(r'''\delta^{p?}_{a} \eta^{a q?} -> \eta^{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{p?}_{a} \eta^{q? a} -> \eta^{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \eta_{a q?} -> \eta_{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \eta_{q? a} -> \eta_{p? q?}'''), repeat=True)

def subs_delta_epsilon(ex):
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{q? r? s? a} -> \epsilon_{q? r? s? p?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{q? r? a s?} -> \epsilon_{q? r? p? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{q? a r? s?} -> \epsilon_{q? p? r? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{a q? r? s?} -> \epsilon_{p? q? r? s?}'''), repeat=True)

    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{q? r? s? a} -> \epsilon^{q? r? s? p?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{q? r? a s?} -> \epsilon^{q? r? p? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{q? a r? s?} -> \epsilon^{q? p? r? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{a q? r? s?} -> \epsilon^{p? q? r? s?}'''), repeat=True)

def subs_eta_epsilon(ex):
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{p? q? r? a} -> \epsilon_{p? q? r? 0}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{p? q? a r?} -> \epsilon_{p? q? 0 r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{p? a q? r?} -> \epsilon_{p? 0 q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{a p? q? r?} -> \epsilon_{0 p? q? r?}'''), repeat=True)

    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{p? q? r? a} -> \epsilon_{p? q? r? 0}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{p? q? a r?} -> \epsilon_{p? q? 0 r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{p? a q? r?} -> \epsilon_{p? 0 q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{a p? q? r?} -> \epsilon_{0 p? q? r?}'''), repeat=True)

    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{p? q? r? a} -> -\gamma^{\alpha \mu} \epsilon_{p? q? r? \mu}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{p? q? a r?} -> -\gamma^{\alpha \mu} \epsilon_{p? q? \mu r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{p? a q? r?} -> -\gamma^{\alpha \mu} \epsilon_{p? \mu q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{a p? q? r?} -> -\gamma^{\alpha \mu} \epsilon_{\mu p? q? r?}'''), repeat=True)

    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{p? q? r? a} -> -\gamma^{\alpha \mu} \epsilon_{p? q? r? \mu}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{p? q? a r?} -> -\gamma^{\alpha \mu} \epsilon_{p? q? \mu r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{p? a q? r?} -> -\gamma^{\alpha \mu} \epsilon_{p? \mu q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{a p? q? r?} -> -\gamma^{\alpha \mu} \epsilon_{\mu p? q? r?}'''), repeat=True)

def normalize_delta(ex):
    substitute(ex, Ex(r'''\delta_{p?}^{q?} -> \delta^{q?}_{p?}'''), repeat=True)

def my_canonicalise(ex):
    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)
    collect_terms(ex)

def three_plus_one(ex):
    eliminate_eta(ex)
    three_plus_one_eta(ex)

    distribute(ex, repeat=True)

    normalize_delta(ex)
    my_eliminate_kronecker(ex)
    three_plus_one_delta(ex)
    
    three_plus_one_epsilon(ex)
    subs_delta_eta(ex)
    
    my_canonicalise(ex)

    normalize_delta(ex)
    subs_delta_epsilon(ex)
    subs_eta_epsilon(ex)

    three_plus_one_delta(ex)
    three_plus_one_epsilon(ex)
    three_plus_one_eta(ex)

    my_canonicalise(ex)

    substitute(ex, ruleH1, repeat=True)
    substitute(ex, ruleH2, repeat=True)
    substitute(ex, ruleH3, repeat=True)

    distribute(ex)
    unwrap(ex)

    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    
    distribute(ex)

    my_canonicalise(ex)
    
    rewrite_indices(ex, Ex(r'\epsilon_{\alpha \beta \gamma}'), Ex(r'\gamma^{\alpha \beta}'))

    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    
    my_canonicalise(ex)
    
    substitute(ex, ruleX)
    substitute(ex, ruleY)
    substitute(ex, ruleZ)
    
    unwrap(ex)
    distribute(ex)
    
    substitute(ex, ruleTraceFree1, repeat=True)
    substitute(ex, ruleTraceFree2, repeat=True)
    substitute(ex, ruleTraceFree3, repeat=True)
    
    distribute(ex)
    
    my_canonicalise(ex)
    
    return(ex)

def kin_ApBq():
    ruleM1  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? d?} \eta^{e? f?} \eta^{g? h?} \eta^{i? j?}''')
    ruleM2  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? d?} \eta^{e? j?} \eta^{f? i?} \eta^{g? h?}''')
    ruleM3  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? e?} \eta^{d? f?} \eta^{g? h?} \eta^{i? j?}''')
    ruleM4  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? f?} \eta^{d? h?} \eta^{e? g?} \eta^{i? j?}''')
    ruleM5  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? f?} \eta^{d? h?} \eta^{e? j?} \eta^{g? i?}''')
    ruleM6  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? c?} \eta^{b? f?} \eta^{d? j?} \eta^{e? h?} \eta^{g? i?}''')
    ruleM7  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? e?} \eta^{b? f?} \eta^{c? g?} \eta^{d? h?} \eta^{i? j?}''')
    ruleM8  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? e?} \eta^{b? f?} \eta^{c? h?} \eta^{d? i?} \eta^{g? j?}''')
    ruleM9  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \eta^{a? f?} \eta^{b? g?} \eta^{c? h?} \eta^{d? i?} \eta^{e? j?}''')
    ruleM10 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? c? d?} \eta^{e? f?} \eta^{g? h?} \eta^{i? j?}''')
    ruleM11 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? c? d?} \eta^{e? j?} \eta^{f? h?} \eta^{g? i?}''')
    ruleM12 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? e? f?} \eta^{c? g?} \eta^{d? h?} \eta^{i? j?}''')
    ruleM13 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? e? f?} \eta^{c? h?} \eta^{d? j?} \eta^{g? i?}''')
    ruleM14 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? f? g?} \eta^{c? e?} \eta^{d? h?} \eta^{i? j?}''')
    ruleM15 = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} -> \epsilon^{a? b? f? g?} \eta^{c? h?} \eta^{d? i?} \eta^{e? j?}''')
    
    ruleM  = Ex(r''' M^{a? b? c? d? e? f? g? h? i? j?} ->e{1} * M{1}^{a? b? c? d? e? f? g? h? i? j?} + e{2} * M{2}^{a? b? c? d? e? f? g? h? i? j?} + e{3} * M{3}^{a? b? c? d? e? f? g? h? i? j?} + e{4} * M{4}^{a? b? c? d? e? f? g? h? i? j?} + e{5} * M{5}^{a? b? c? d? e? f? g? h? i? j?} + e{6} * M{6}^{a? b? c? d? e? f? g? h? i? j?} + e{7} * M{7}^{a? b? c? d? e? f? g? h? i? j?} + e{8} * M{8}^{a? b? c? d? e? f? g? h? i? j?} + e{9} * M{9}^{a? b? c? d? e? f? g? h? i? j?} + e{10} * M{10}^{a? b? c? d? e? f? g? h? i? j?} + e{11} * M{11}^{a? b? c? d? e? f? g? h? i? j?} + e{12} * M{12}^{a? b? c? d? e? f? g? h? i? j?} + e{13} * M{13}^{a? b? c? d? e? f? g? h? i? j?} + e{14} * M{14}^{a? b? c? d? e? f? g? h? i? j?} + e{15} * M{15}^{a? b? c? d? e? f? g? h? i? j?}''')
    
    ruleMH1  = Ex(r''' M^{a b c d e f? g? h? i? j?} \partial_{e}{H_{a b c d}} ->(M^{0 \mu 0 \nu 0 f? g? h? i? j?} - M^{0 \mu \nu 0 0 f? g? h? i? j?} - M^{\mu 0 0 \nu 0 f? g? h? i? j?} + M^{\mu 0 \nu 0 0 f? g? h? i? j?}) \partial_{0}{H1_{\mu \nu}} + (M^{0 \mu 0 \nu \alpha f? g? h? i? j?} - M^{0 \mu \nu 0 \alpha f? g? h? i? j?} - M^{\mu 0 0 \nu \alpha f? g? h? i? j?} + M^{\mu 0 \nu 0 \alpha f? g? h? i? j?}) \partial_{\alpha}{H1_{\mu \nu}} + (M^{0 \mu \nu \rho 0 f? g? h? i? j?} - M^{\mu 0 \nu \rho 0 f? g? h? i? j?} + M^{\nu \rho 0 \mu 0 f? g? h? i? j?} - M^{\nu \rho \mu 0 0 f? g? h? i? j?}) \partial_{0}{H2_{\mu \nu \rho}} + (M^{0 \mu \nu \rho \alpha f? g? h? i? j?} - M^{\mu 0 \nu \rho \alpha f? g? h? i? j?} + M^{\nu \rho 0 \mu \alpha f? g? h? i? j?} - M^{\nu \rho \mu 0 \alpha f? g? h? i? j?}) \partial_{\alpha}{H2_{\mu \nu \rho}} + M^{\mu \nu \rho \sigma 0 f? g? h? i? j?} \partial_{0}{H3_{\mu \nu \rho \sigma}} + M^{\mu \nu \rho \sigma \alpha f? g? h? i? j?} \partial_{\alpha}{H3_{\mu \nu \rho \sigma}}''')
    
    ruleMH2  = Ex(r''' M^{f? g? h? i? j? a b c d e} \partial_{e}{H_{a b c d}} ->(M^{f? g? h? i? j? 0 \mu 0 \nu 0} - M^{f? g? h? i? j? 0 \mu \nu 0 0} - M^{f? g? h? i? j? \mu 0 0 \nu 0} + M^{f? g? h? i? j? \mu 0 \nu 0 0}) \partial_{0}{H1_{\mu \nu}} + (M^{f? g? h? i? j? 0 \mu 0 \nu \alpha} - M^{f? g? h? i? j? 0 \mu \nu 0 \alpha} - M^{f? g? h? i? j? \mu 0 0 \nu \alpha} + M^{f? g? h? i? j? \mu 0 \nu 0 \alpha}) \partial_{\alpha}{H1_{\mu \nu}} + (M^{f? g? h? i? j? 0 \mu \nu \rho 0} - M^{f? g? h? i? j? \mu 0 \nu \rho 0} + M^{f? g? h? i? j? \nu \rho 0 \mu 0} - M^{f? g? h? i? j? \nu \rho \mu 0 0}) \partial_{0}{H2_{\mu \nu \rho}} + (M^{f? g? h? i? j? 0 \mu \nu \rho \alpha} - M^{f? g? h? i? j? \mu 0 \nu \rho \alpha} + M^{f? g? h? i? j? \nu \rho 0 \mu \alpha} - M^{f? g? h? i? j? \nu \rho \mu 0 \alpha}) \partial_{\alpha}{H2_{\mu \nu \rho}} + M^{f? g? h? i? j? \mu \nu \rho \sigma 0} \partial_{0}{H3_{\mu \nu \rho \sigma}} + M^{f? g? h? i? j? \mu \nu \rho \sigma \alpha} \partial_{\alpha}{H3_{\mu \nu \rho \sigma}}''')
    
    ex  = Ex(r''' M^{a b c d e f g h i j} \partial_{e}{H_{a b c d}} \partial_{j}{H_{f g h i}}''')
    
    
    substitute(ex, ruleMH1)
    distribute(ex)
    substitute(ex, ruleMH2)
    distribute(ex)
    
    
    substitute(ex, ruleM)
    substitute(ex, ruleM1)
    substitute(ex, ruleM2)
    substitute(ex, ruleM3)
    substitute(ex, ruleM4)
    substitute(ex, ruleM5)
    substitute(ex, ruleM6)
    substitute(ex, ruleM7)
    substitute(ex, ruleM8)
    substitute(ex, ruleM9)
    substitute(ex, ruleM10)
    substitute(ex, ruleM11)
    substitute(ex, ruleM12)
    substitute(ex, ruleM13)
    substitute(ex, ruleM14)
    substitute(ex, ruleM15)
    
    three_plus_one(ex)

    return(ex)

def mass_AB():
    ruleM1  = Ex(r''' M{1}_{a? b? c? d? e? f? g? h?} ->\eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? h?}''')
    ruleM2  = Ex(r''' M{2}_{a? b? c? d? e? f? g? h?} ->\eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? h?}''')
    ruleM3  = Ex(r''' M{3}_{a? b? c? d? e? f? g? h?} ->\eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? h?}''')
    ruleM4  = Ex(r''' M{4}_{a? b? c? d? e? f? g? h?} ->\eta_{a? e?} \eta_{b? g?} \eta_{c? f?} \eta_{d? h?}''')
    ruleM5  = Ex(r''' M{5}_{a? b? c? d? e? f? g? h?} ->\epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? h?}''')
    ruleM6  = Ex(r''' M{6}_{a? b? c? d? e? f? g? h?} ->\epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? h?}''')
    
    ruleM  = Ex(r''' M_{a? b? c? d? e? f? g? h?} ->e{1} * M{1}_{a? b? c? d? e? f? g? h?} + e{2} * M{2}_{a? b? c? d? e? f? g? h?} + e{3} * M{3}_{a? b? c? d? e? f? g? h?} + e{4} * M{4}_{a? b? c? d? e? f? g? h?} + e{5} * M{5}_{a? b? c? d? e? f? g? h?} + e{6} * M{6}_{a? b? c? d? e? f? g? h?}''')
    
    ruleMH1  = Ex(r''' M_{a b c d e? f? g? h?} H^{a b c d} ->(M_{0 \mu 0 \nu e? f? g? h?} - M_{0 \mu \nu 0 e? f? g? h?} - M_{\mu 0 0 \nu e? f? g? h?} + M_{\mu 0 \nu 0 e? f? g? h?}) H1^{\mu \nu} + (M_{0 \mu \nu \rho e? f? g? h?} - M_{\mu 0 \nu \rho e? f? g? h?} + M_{\nu \rho 0 \mu e? f? g? h?} - M_{\nu \rho \mu 0 e? f? g? h?}) H2^{\mu \nu \rho} + M_{\mu \nu \rho \sigma e? f? g? h?} H3^{\mu \nu \rho \sigma}''')
    
    ruleMH2  = Ex(r''' M_{e? f? g? h? a b c d} H^{a b c d} ->(M_{e? f? g? h? 0 \mu 0 \nu} - M_{e? f? g? h? 0 \mu \nu 0} - M_{e? f? g? h? \mu 0 0 \nu} + M_{e? f? g? h? \mu 0 \nu 0}) H1^{\mu \nu} + (M_{e? f? g? h? 0 \mu \nu \rho} - M_{e? f? g? h? \mu 0 \nu \rho} + M_{e? f? g? h? \nu \rho 0 \mu} - M_{e? f? g? h? \nu \rho \mu 0}) H2^{\mu \nu \rho} + M_{e? f? g? h? \mu \nu \rho \sigma} H3^{\mu \nu \rho \sigma}''')
    
    ex  = Ex(r''' M_{a b c d e f g h} H^{a b c d} H^{e f g h}''')
    
    substitute(ex, ruleMH1)
    distribute(ex)
    substitute(ex, ruleMH2)
    distribute(ex)
    
    substitute(ex, ruleM)
    substitute(ex, ruleM1)
    substitute(ex, ruleM2)
    substitute(ex, ruleM3)
    substitute(ex, ruleM4)
    substitute(ex, ruleM5)
    substitute(ex, ruleM6)
    
    three_plus_one(ex)
    
    return(ex)

def save_all():
  save_AB()
  save_ApBq()
  save_ABI()

def save_AB():
    ex = mass_AB()
    with open("mass_AB.cdb", "w") as file:
      file.write(ex.input_form()+"\n")

def save_ApBq():
    ex = kin_ApBq()
    with open("kin_ApBq.cdb", "w") as file:
      file.write(ex.input_form()+"\n")

def save_ABI():
    ex = kin_ABI()
    with open("kin_ABI.cdb", "w") as file:
      file.write(ex.input_form()+"\n")

def load_AB():
    with open("mass_AB.cdb", "r") as file:
      ex = Ex(file.readline())
    return(ex)

def load_ApBq():
    with open("kin_ApBq.cdb", "r") as file:
      ex = Ex(file.readline())
    return(ex)

def load_ABI():
    with open("kin_ABI.cdb", "r") as file:
      ex = Ex(file.readline())
    return(ex)

def eom(massAB, kinABI, kinApBq, toVary):
    substitute(kinABI, Ex(r'e{1} -> e{22}'))
    substitute(kinABI, Ex(r'e{2} -> e{23}'))
    substitute(kinABI, Ex(r'e{3} -> e{24}'))
    substitute(kinABI, Ex(r'e{4} -> e{25}'))
    substitute(kinABI, Ex(r'e{5} -> e{26}'))
    substitute(kinABI, Ex(r'e{6} -> e{27}'))
    substitute(kinABI, Ex(r'e{7} -> e{28}'))
    substitute(kinABI, Ex(r'e{8} -> e{29}'))
    substitute(kinABI, Ex(r'e{9} -> e{30}'))
    substitute(kinABI, Ex(r'e{10} -> e{31}'))
    substitute(kinABI, Ex(r'e{11} -> e{32}'))
    substitute(kinABI, Ex(r'e{12} -> e{33}'))
    substitute(kinABI, Ex(r'e{13} -> e{34}'))
    substitute(kinABI, Ex(r'e{14} -> e{35}'))
    substitute(kinABI, Ex(r'e{15} -> e{36}'))
    substitute(kinABI, Ex(r'e{16} -> e{37}'))

    substitute(kinApBq, Ex(r'e{1} -> e{7}'))
    substitute(kinApBq, Ex(r'e{2} -> e{8}'))
    substitute(kinApBq, Ex(r'e{3} -> e{9}'))
    substitute(kinApBq, Ex(r'e{4} -> e{10}'))
    substitute(kinApBq, Ex(r'e{5} -> e{11}'))
    substitute(kinApBq, Ex(r'e{6} -> e{12}'))
    substitute(kinApBq, Ex(r'e{7} -> e{13}'))
    substitute(kinApBq, Ex(r'e{8} -> e{14}'))
    substitute(kinApBq, Ex(r'e{9} -> e{15}'))
    substitute(kinApBq, Ex(r'e{10} -> e{16}'))
    substitute(kinApBq, Ex(r'e{11} -> e{17}'))
    substitute(kinApBq, Ex(r'e{12} -> e{18}'))
    substitute(kinApBq, Ex(r'e{13} -> e{19}'))
    substitute(kinApBq, Ex(r'e{14} -> e{20}'))
    substitute(kinApBq, Ex(r'e{15} -> e{21}'))

    apply_sol(massAB)
    apply_sol(kinABI)
    apply_sol(kinApBq)

    variation = Ex(r'd' + toVary.input_form())
    ruleVary = Ex(r'@{toVary} -> @{variation}')

    ex = Ex(r'\int{@(massAB) + @(kinABI) + @(kinApBq)}{x}')

    distribute(ex, repeat=True)
    my_canonicalise(ex)

    vary(ex, ruleVary)

    integrate_by_parts(ex, Ex(r'\partial_{\alpha?}{@(variation)}'), repeat=True)
    unwrap(ex, repeat=True)
    product_rule(ex, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    integrate_by_parts(ex, variation, repeat=True)
    unwrap(ex, repeat=True)
    product_rule(ex, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    factor_out(ex, variation)

    return ex

def eom_from_files(toVary):
    ex1 = load_AB()
    ex2 = load_ABI()
    ex3 = load_ApBq()

    my_eliminate_metric(ex1)
    eliminate_kronecker(ex1, repeat=True)
    my_canonicalise(ex1)
    substitute(ex1, ruleTraceFree1)
    substitute(ex1, ruleTraceFree2)

    my_eliminate_metric(ex2)
    eliminate_kronecker(ex2, repeat=True)
    my_canonicalise(ex2)
    substitute(ex2, ruleTraceFree1)
    substitute(ex2, ruleTraceFree2)

    my_eliminate_metric(ex3)
    eliminate_kronecker(ex3, repeat=True)
    my_canonicalise(ex3)
    substitute(ex3, ruleTraceFree1)
    substitute(ex3, ruleTraceFree2)

    return eom(ex1, ex2, ex3, toVary)

def apply_sol(ex):
  substitute(ex, Ex(r'''e{1} -> 1/2*k{1} + (-1)*k{2} + (-1/3)*k{3}'''))
  substitute(ex, Ex(r'''e{2} -> (-3)*k{1} + 12*k{2} + 4*k{3}'''))
  substitute(ex, Ex(r'''e{3} -> 1*k{1} + (-6)*k{2} + (-2)*k{3}'''))
  substitute(ex, Ex(r'''e{4} -> 1*k{1}'''))
  substitute(ex, Ex(r'''e{5} -> 1*k{2}'''))
  substitute(ex, Ex(r'''e{6} -> 1*k{3}'''))
  substitute(ex, Ex(r'''e{7} -> (-1/2)*k{4} + 1*k{5} + 3*k{9} + 3/2*k{10} + 1/4*k{11} + (-3/8)*k{12} + (-3/4)*k{13} + (-7/64)*k{16}'''))
  substitute(ex, Ex(r'''e{8} -> (-1/24)*k{4} + 5/24*k{5} + 1/6*k{6} + 3/2*k{9} + 3/4*k{10} + 1/8*k{11} + (-3/16)*k{12} + (-3/8)*k{13} + (-1/32)*k{16}'''))
  substitute(ex, Ex(r'''e{9} -> 3/4*k{4} + (-3/2)*k{5} + 3/32*k{16}'''))
  substitute(ex, Ex(r'''e{10} -> (-1)*k{4} + 2*k{5} + (-1/8)*k{16}'''))
  substitute(ex, Ex(r'''e{11} -> 1/4*k{4} + (-1/2)*k{5} + (-2)*k{6} + (-6)*k{9} + (-3)*k{10} + (-1/2)*k{11} + 3/4*k{12} + 3/2*k{13} + 7/64*k{16}'''))
  substitute(ex, Ex(r'''e{12} -> (-1/4)*k{4} + 1/2*k{5} + (-1/16)*k{16}'''))
  substitute(ex, Ex(r'''e{13} -> 1*k{4}'''))
  substitute(ex, Ex(r'''e{14} -> 1*k{5}'''))
  substitute(ex, Ex(r'''e{15} -> 1*k{6}'''))
  substitute(ex, Ex(r'''e{16} -> (-1/8)*k{4} + (-1/8)*k{5} + 1/2*k{6} + 3*k{7} + 1*k{8} + 3/2*k{9} + 3/4*k{10} + 1/8*k{11} + (-3/16)*k{12} + (-3/8)*k{13} + (-1/128)*k{16}'''))
  substitute(ex, Ex(r'''e{17} -> 1*k{7}'''))
  substitute(ex, Ex(r'''e{18} -> (-3/8)*k{4} + (-3/8)*k{5} + 3/2*k{6} + 9*k{7} + 3*k{8}'''))
  substitute(ex, Ex(r'''e{19} -> (-1/8)*k{4} + (-1/8)*k{5} + 1/2*k{6} + 3*k{7} + 1*k{8}'''))
  substitute(ex, Ex(r'''e{20} -> 1/16*k{4} + 1/16*k{5} + (-1/4)*k{6} + (-3/2)*k{7} + (-1/2)*k{8}'''))
  substitute(ex, Ex(r'''e{21} -> 1*k{8}'''))
  substitute(ex, Ex(r'''e{22} -> 1*k{9}'''))
  substitute(ex, Ex(r'''e{23} -> 1*k{10}'''))
  substitute(ex, Ex(r'''e{24} -> 1*k{11}'''))
  substitute(ex, Ex(r'''e{25} -> (-1)*k{12} + (-1/16)*k{16}'''))
  substitute(ex, Ex(r'''e{26} -> 1*k{12} + 1/8*k{16}'''))
  substitute(ex, Ex(r'''e{27} -> (-3)*k{9} + (-3/2)*k{10} + (-1/4)*k{11} + 3/8*k{12} + 3/4*k{13} + 3/64*k{16}'''))
  substitute(ex, Ex(r'''e{28} -> (-3)*k{9} + (-3/2)*k{10} + (-3/4)*k{11} + 3/8*k{12} + 1/4*k{13} + 3/64*k{16}'''))
  substitute(ex, Ex(r'''e{29} -> 1*k{12}'''))
  substitute(ex, Ex(r'''e{30} -> 1*k{13}'''))
  substitute(ex, Ex(r'''e{31} -> (-1/4)*k{10} + 1/24*k{11} + 1/16*k{12} + 1/8*k{13} + (-1/6)*k{14} + 1/128*k{16}'''))
  substitute(ex, Ex(r'''e{32} -> 1/2*k{10} + (-1/6)*k{12} + (-1/3)*k{15} + (-1/48)*k{16}'''))
  substitute(ex, Ex(r'''e{33} -> 1*k{14}'''))
  substitute(ex, Ex(r'''e{34} -> 1*k{15}'''))
  substitute(ex, Ex(r'''e{35} -> 6*k{9} + 3*k{10} + 1/2*k{11} + (-3/4)*k{12} + (-3/2)*k{13} + (-1/32)*k{16}'''))
  substitute(ex, Ex(r'''e{36} -> 3*k{9} + 3/2*k{10} + 1/4*k{11} + (-3/8)*k{12} + (-3/4)*k{13} + 1*k{15} + (-1/64)*k{16}'''))
  substitute(ex, Ex(r'''e{37} -> (-1/4)*k{9} + (-1/8)*k{10} + 1/48*k{11} + 1/96*k{12} + 3/16*k{13} + (-1/6)*k{14} + (-1/12)*k{15} + (-1/768)*k{16}'''))
  substitute(ex, Ex(r'''e{38} -> 48*k{9} + 24*k{10} + 4*k{11} + (-6)*k{12} + (-12)*k{13} + (-3/4)*k{16}'''))
  substitute(ex, Ex(r'''e{39} -> 1*k{16}'''))
  substitute(ex, Ex(r'''e{40} -> 24*k{9} + 12*k{10} + 2*k{11} + (-3)*k{12} + (-6)*k{13} + (-1/8)*k{16}'''))
  return(ex)
