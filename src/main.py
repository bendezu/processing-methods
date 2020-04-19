import copy
import numpy as np

from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult, mult_const
from src.filter.bandpass import bandpass
from src.filter.bandstop import bandstop, bsf_pic, bsf_line
from src.filter.highpass import hpf_line, hpf_pic
from src.filter.lowpass import lpf_line, lpf_pic
from src.line.Line import Line
from src.line.cardiogram import ecg, base, delta
from src.picture.Picture import Picture
from src.picture.filtering import mean_filter, median_filter
from src.picture.noising import gaussian_noise, salt_and_pepper, all_noise
from src.picture.operations import or_pic, xor_pic, and_pic
from src.picture.postprocessing import neg, gamma, log, transform, deconv_pic, reg_deconv_pic, diff_pic
from src.picture.scaling import scale
from src.picture.segmentation import thresholding, sobel
from src.picture.statistic import histogram, cdf
from src.transform.convolution import conv, deconv, reg_deconv
from src.transform.hammingwindow import window
from src.util.buider import const, line, rand, sub, absolute, cross, auto, anti_trend, harmonic, spikes, dft, diff

canvas = Canvas()
io = IOController()

def lesson0():
    first = base()
    second = delta()
    convolution = conv(first, second)
    return np.array([
        (first, second),
        (convolution, deconv(convolution, first))
    ])

def lesson1():
    img = io.read_from_jpg("grace.jpg")
    return np.array([
        (img, scale(img, ratio=3, strategy="nearest-neighbor"), scale(img, ratio=0.5, strategy="nearest-neighbor")),
        (img, scale(img, ratio=3, strategy="bilinear"), scale(img, ratio=0.5, strategy="bilinear"))
    ])

def lesson2():
    img1 = io.read_from_jpg("image1.jpg")
    img2 = io.read_from_jpg("image2.jpg")
    return np.array([
        (neg(img1), neg(img2)),
        (gamma(img1, C=1, gamma=1.1), gamma(img2, C=1, gamma=0.3)),
        (log(img1, C=1), log(img2, C=1))
    ])

def lesson3():
    img = io.read_from_jpg("HollywoodLC-1.jpg")
    img2 = transform(img, cdf(img))
    return np.array([
        (img, histogram(img)),
        (img, cdf(img)),
        (img2, histogram(img2))
    ])

def lesson4():
    xcr = io.read_from_xcr('h400x300.xcr')
    sample_line = Line("line", y=xcr.matrix[100])
    bs_line = bsf_line(sample_line, lowcut=100, highcut=150)
    bs_pic = bsf_pic(xcr, lowcut=100, highcut=150)
    return np.array([
        (xcr, auto(sample_line)),
        (xcr, dft(auto(sample_line), scale=True)),
        (bs_pic, auto(bs_line)),
        (bs_pic, dft(auto(bs_line), scale=True))
    ])

def lesson5():
    img = io.read_from_jpg('MODEL.jpg')
    gauss1 = gaussian_noise(img, percent=0.01)
    gauss5 = gaussian_noise(img, percent=0.05)
    gauss15 = gaussian_noise(img, percent=0.15)
    snp = salt_and_pepper(img, percent=0.05)
    all = all_noise(img, gaus_percent=0.15, snp_percent=0.05)

    # noises
    # return np.array([
    #     (gauss1, gauss5, gauss15),
    #     (img, snp, all),
    # ])

    # histograms
    # return np.array([
    #     (gauss5, histogram(gauss5)),
    #     (snp, histogram(snp)),
    #     (all, histogram(all)),
    # ])

    line_idx = 200
    i_line = img.get_line(line_idx)
    g5_line = gauss5.get_line(line_idx)
    sp_line = snp.get_line(line_idx)
    a_line = all.get_line(line_idx)

    i_dft = dft(i_line, scale=True)
    g5_dft = dft(g5_line, scale=True)
    sp_dft = dft(sp_line, scale=True)
    a_dft = dft(a_line, scale=True)

    # line and line dft
    # return np.array([
    #     (img, i_line, i_dft),
    #     (gauss5, g5_line, g5_dft),
    #     (snp, sp_line, sp_dft),
    #     (all, a_line, a_dft),
    # ])

    i_auto_line = auto(i_line)
    g5_auto_line = auto(g5_line)
    sp_auto_line = auto(sp_line)
    a_auto_line = auto(a_line)

    i_dft_auto = dft(i_auto_line, scale=True)
    g5_dft_auto = dft(g5_auto_line, scale=True)
    sp_dft_auto = dft(sp_auto_line, scale=True)
    a_dft_auto = dft(a_auto_line, scale=True)

    # auto line and auto line dft
    # return np.array([
    #     (img, i_auto_line, i_dft_auto),
    #     (gauss5, g5_auto_line, g5_dft_auto),
    #     (snp, sp_auto_line, sp_dft_auto),
    #     (all, a_auto_line, a_dft_auto),
    # ])

    cut = 15
    g5_lpf = lpf_pic(gauss5, cut)
    sp_lpf = lpf_pic(snp, cut)
    a_lpf = lpf_pic(all, cut)

    g5_line_lpf = lpf_line(g5_line, cut)
    sp_line_lpf = lpf_line(sp_line, cut)
    a_line_lpf = lpf_line(a_line, cut)

    # filtered images
    return np.array([
        (img, i_line, i_dft),
        (g5_lpf, g5_line_lpf, dft(g5_line_lpf, scale=True)),
        (sp_lpf, sp_line_lpf, dft(sp_line_lpf, scale=True)),
        (a_lpf, a_line_lpf, dft(a_line_lpf, scale=True)),
    ])

def lesson6():
    img = io.read_from_jpg('MODEL.jpg')
    gauss1 = gaussian_noise(img, percent=0.01)
    gauss5 = gaussian_noise(img, percent=0.05)
    gauss15 = gaussian_noise(img, percent=0.15)
    snp1 = salt_and_pepper(img, percent=0.01)
    snp5 = salt_and_pepper(img, percent=0.05)
    snp15 = salt_and_pepper(img, percent=0.15)
    all1 = all_noise(img, gaus_percent=0.01, snp_percent=0.01)
    all5 = all_noise(img, gaus_percent=0.05, snp_percent=0.05)
    all15 = all_noise(img, gaus_percent=0.15, snp_percent=0.15)

    # return np.array([
    #     (gauss1, gauss5, gauss15),
    #     (snp1, snp5, snp15),
    #     (all1, all5, all15),
    # ])

    # return np.array([
    #     (mean_filter(gauss1, size=5), mean_filter(gauss5, size=7), mean_filter(gauss15, size=11)),
    #     (mean_filter(snp1, size=7), mean_filter(snp5, size=11), mean_filter(snp15, size=13)),
    #     (mean_filter(all1, size=11), mean_filter(all5, size=15), mean_filter(all15, size=21)),
    # ])

    return np.array([
        (median_filter(gauss1, size=3), median_filter(gauss5, size=7), median_filter(gauss15, size=15)),
        (median_filter(snp1, size=3), median_filter(snp5, size=3), median_filter(snp15, size=5)),
        (median_filter(all1, size=5), median_filter(all5, size=11), median_filter(all15, size=25)),
    ])

def lesson7():
    kernel = io.read_from_dat("kernL64_f4.dat")
    blurred = io.read_img_from_dat("blur259x185L.dat")
    blurred_noised = io.read_img_from_dat("blur259x185L_N.dat")

    padded_kernel = concat(kernel, const(value=0, n=259-kernel.getN()))
    dft_kernel = dft(padded_kernel, scale=True)
    b_line = blurred.get_line(110)
    bn_line = blurred_noised.get_line(110)

    # return np.array([
    #     (padded_kernel, dft_kernel),
    #     (blurred, blurred_noised),
    #     (b_line, bn_line),
    # ])

    # dft_b_line = dft(b_line, scale=True)
    # deconv_b_line = deconv(b_line, padded_kernel)
    # deconv_b = deconv_pic(blurred, padded_kernel)
    #
    # return np.array([
    #     (deconv_b, dft_b_line),
    #     (deconv_b_line, dft(deconv_b_line, scale=True)),
    # ])

    dft_bn_line = dft(bn_line, scale=True)
    deconv_bn_line = reg_deconv(bn_line, padded_kernel, k=0.0001)
    deconv_bn = reg_deconv_pic(blurred_noised, padded_kernel, k=0.0001)

    return np.array([
        (blurred_noised, dft_bn_line),
        (deconv_bn, deconv_bn_line),
    ])

def lesson8():
    img = io.read_from_jpg("MODEL.jpg")
    thresh_img = thresholding(img, thresh=200)
    diff_thresh_img = diff_pic(thresh_img) # contour
    hpf_img = hpf_pic(img, cut=167) # contour

    noised = gaussian_noise(img, percent=0.15)
    thresh_noised = thresholding(noised, thresh=200)
    lpf = lpf_pic(noised, cut=10)
    hpf = hpf_pic(noised, cut=10)
    white = thresholding(lpf, thresh=130) # part of contour

    l1 = lpf_pic(thresh_noised, cut=15)
    t1 = thresholding(l1, thresh=80)
    l2 = lpf_pic(t1, cut=15)
    d2 = diff_pic(l2)
    t2 = thresholding(d2, thresh=30) # contour

    median = median_filter(thresh_noised, size=5)
    diff_median = diff_pic(median) # contour
    return np.array([
        (noised, thresh_noised, median, diff_median),
        (l2, d2, t2, sobel(median)),
    ])

plotables = lesson8()
canvas.set_plotables(plotables)
figure = canvas.plot()

io.savePlotToFile(figure, "result")
