<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: 2cb530243943 Lib/hashlib.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="https://hg.python.org">
<img src="/cpython/static/hglogo.png" alt="mercurial" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/3.5">log</a></li>
<li><a href="/cpython/graph/3.5">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/bookmarks">bookmarks</a></li>
<li><a href="/cpython/branches">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/3.5">changeset</a></li>
<li><a href="/cpython/file/3.5/Lib/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/hashlib.py">latest</a></li>
<li><a href="/cpython/diff/3.5/Lib/hashlib.py">diff</a></li>
<li><a href="/cpython/comparison/3.5/Lib/hashlib.py">comparison</a></li>
<li><a href="/cpython/annotate/3.5/Lib/hashlib.py">annotate</a></li>
<li><a href="/cpython/log/3.5/Lib/hashlib.py">file log</a></li>
<li><a href="/cpython/raw-file/3.5/Lib/hashlib.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2 class="breadcrumb"><a href="/">Mercurial</a> &gt; <a href="/cpython">cpython</a> </h2>
<h3>
 view Lib/hashlib.py @ 106485:<a href="/cpython/rev/2cb530243943">2cb530243943</a>
 <span class="branchhead">3.5</span> 
</h3>


<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" value="" /></p>
<div id="hint">Find changesets by keywords (author, files, the commit message), revision
number or hash, or <a href="/cpython/help/revsets">revset expression</a>.</div>
</form>

<div class="description">Fix #29519: weakref spewing exceptions during interp finalization</a> [<a href="http://bugs.python.org/29519" class="issuelink">#29519</a>]</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#321;&#117;&#107;&#97;&#115;&#122;&#32;&#76;&#97;&#110;&#103;&#97;&#32;&#60;&#108;&#117;&#107;&#97;&#115;&#122;&#64;&#108;&#97;&#110;&#103;&#97;&#46;&#112;&#108;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Fri, 10 Feb 2017 00:14:55 -0800</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/a4f3e78f68e4/Lib/hashlib.py">a4f3e78f68e4</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"><a href="/cpython/file/d926fa1a833c/Lib/hashlib.py">d926fa1a833c</a> </td>
</tr>
</table>

<div class="overflow">
<div class="sourcefirst linewraptoggle">line wrap: <a class="linewraplink" href="javascript:toggleLinewrap()">on</a></div>
<div class="sourcefirst"> line source</div>
<pre class="sourcelines stripes4 wrap bottomline"
     data-logurl="/cpython/log/3.5/Lib/hashlib.py"
     data-selectabletag="SPAN"
     data-ishead="0">

<span id="l1"><span class="c1">#.  Copyright (C) 2005-2010   Gregory P. Smith (greg@krypto.org)</span></span><a href="#l1"></a>
<span id="l2"><span class="c1">#  Licensed to PSF under a Contributor Agreement.</span></span><a href="#l2"></a>
<span id="l3"><span class="c1">#</span></span><a href="#l3"></a>
<span id="l4"></span><a href="#l4"></a>
<span id="l5"><span class="vm">__doc__</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;hashlib module - A common interface to many hash functions.</span></span><a href="#l5"></a>
<span id="l6"></span><a href="#l6"></a>
<span id="l7"><span class="s2">new(name, data=b&#39;&#39;) - returns a new hash object implementing the</span></span><a href="#l7"></a>
<span id="l8"><span class="s2">                      given hash function; initializing the hash</span></span><a href="#l8"></a>
<span id="l9"><span class="s2">                      using the given binary data.</span></span><a href="#l9"></a>
<span id="l10"></span><a href="#l10"></a>
<span id="l11"><span class="s2">Named constructor functions are also available, these are faster</span></span><a href="#l11"></a>
<span id="l12"><span class="s2">than using new(name):</span></span><a href="#l12"></a>
<span id="l13"></span><a href="#l13"></a>
<span id="l14"><span class="s2">md5(), sha1(), sha224(), sha256(), sha384(), and sha512()</span></span><a href="#l14"></a>
<span id="l15"></span><a href="#l15"></a>
<span id="l16"><span class="s2">More algorithms may be available on your platform but the above are guaranteed</span></span><a href="#l16"></a>
<span id="l17"><span class="s2">to exist.  See the algorithms_guaranteed and algorithms_available attributes</span></span><a href="#l17"></a>
<span id="l18"><span class="s2">to find out what algorithm names can be passed to new().</span></span><a href="#l18"></a>
<span id="l19"></span><a href="#l19"></a>
<span id="l20"><span class="s2">NOTE: If you want the adler32 or crc32 hash functions they are available in</span></span><a href="#l20"></a>
<span id="l21"><span class="s2">the zlib module.</span></span><a href="#l21"></a>
<span id="l22"></span><a href="#l22"></a>
<span id="l23"><span class="s2">Choose your hash function wisely.  Some have known collision weaknesses.</span></span><a href="#l23"></a>
<span id="l24"><span class="s2">sha384 and sha512 will be slow on 32 bit platforms.</span></span><a href="#l24"></a>
<span id="l25"></span><a href="#l25"></a>
<span id="l26"><span class="s2">Hash objects have these methods:</span></span><a href="#l26"></a>
<span id="l27"><span class="s2"> - update(arg): Update the hash object with the bytes in arg. Repeated calls</span></span><a href="#l27"></a>
<span id="l28"><span class="s2">                are equivalent to a single call with the concatenation of all</span></span><a href="#l28"></a>
<span id="l29"><span class="s2">                the arguments.</span></span><a href="#l29"></a>
<span id="l30"><span class="s2"> - digest():    Return the digest of the bytes passed to the update() method</span></span><a href="#l30"></a>
<span id="l31"><span class="s2">                so far.</span></span><a href="#l31"></a>
<span id="l32"><span class="s2"> - hexdigest(): Like digest() except the digest is returned as a unicode</span></span><a href="#l32"></a>
<span id="l33"><span class="s2">                object of double length, containing only hexadecimal digits.</span></span><a href="#l33"></a>
<span id="l34"><span class="s2"> - copy():      Return a copy (clone) of the hash object. This can be used to</span></span><a href="#l34"></a>
<span id="l35"><span class="s2">                efficiently compute the digests of strings that share a common</span></span><a href="#l35"></a>
<span id="l36"><span class="s2">                initial substring.</span></span><a href="#l36"></a>
<span id="l37"></span><a href="#l37"></a>
<span id="l38"><span class="s2">For example, to obtain the digest of the string &#39;Nobody inspects the</span></span><a href="#l38"></a>
<span id="l39"><span class="s2">spammish repetition&#39;:</span></span><a href="#l39"></a>
<span id="l40"></span><a href="#l40"></a>
<span id="l41"><span class="s2">    &gt;&gt;&gt; import hashlib</span></span><a href="#l41"></a>
<span id="l42"><span class="s2">    &gt;&gt;&gt; m = hashlib.md5()</span></span><a href="#l42"></a>
<span id="l43"><span class="s2">    &gt;&gt;&gt; m.update(b&quot;Nobody inspects&quot;)</span></span><a href="#l43"></a>
<span id="l44"><span class="s2">    &gt;&gt;&gt; m.update(b&quot; the spammish repetition&quot;)</span></span><a href="#l44"></a>
<span id="l45"><span class="s2">    &gt;&gt;&gt; m.digest()</span></span><a href="#l45"></a>
<span id="l46"><span class="s2">    b&#39;</span><span class="se">\\</span><span class="s2">xbbd</span><span class="se">\\</span><span class="s2">x9c</span><span class="se">\\</span><span class="s2">x83</span><span class="se">\\</span><span class="s2">xdd</span><span class="se">\\</span><span class="s2">x1e</span><span class="se">\\</span><span class="s2">xa5</span><span class="se">\\</span><span class="s2">xc9</span><span class="se">\\</span><span class="s2">xd9</span><span class="se">\\</span><span class="s2">xde</span><span class="se">\\</span><span class="s2">xc9</span><span class="se">\\</span><span class="s2">xa1</span><span class="se">\\</span><span class="s2">x8d</span><span class="se">\\</span><span class="s2">xf0</span><span class="se">\\</span><span class="s2">xff</span><span class="se">\\</span><span class="s2">xe9&#39;</span></span><a href="#l46"></a>
<span id="l47"></span><a href="#l47"></a>
<span id="l48"><span class="s2">More condensed:</span></span><a href="#l48"></a>
<span id="l49"></span><a href="#l49"></a>
<span id="l50"><span class="s2">    &gt;&gt;&gt; hashlib.sha224(b&quot;Nobody inspects the spammish repetition&quot;).hexdigest()</span></span><a href="#l50"></a>
<span id="l51"><span class="s2">    &#39;a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2&#39;</span></span><a href="#l51"></a>
<span id="l52"></span><a href="#l52"></a>
<span id="l53"><span class="s2">&quot;&quot;&quot;</span></span><a href="#l53"></a>
<span id="l54"></span><a href="#l54"></a>
<span id="l55"><span class="c1"># This tuple and __get_builtin_constructor() must be modified if a new</span></span><a href="#l55"></a>
<span id="l56"><span class="c1"># always available algorithm is added.</span></span><a href="#l56"></a>
<span id="l57"><span class="n">__always_supported</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;md5&#39;</span><span class="p">,</span> <span class="s1">&#39;sha1&#39;</span><span class="p">,</span> <span class="s1">&#39;sha224&#39;</span><span class="p">,</span> <span class="s1">&#39;sha256&#39;</span><span class="p">,</span> <span class="s1">&#39;sha384&#39;</span><span class="p">,</span> <span class="s1">&#39;sha512&#39;</span><span class="p">)</span></span><a href="#l57"></a>
<span id="l58"></span><a href="#l58"></a>
<span id="l59"><span class="n">algorithms_guaranteed</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">__always_supported</span><span class="p">)</span></span><a href="#l59"></a>
<span id="l60"><span class="n">algorithms_available</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">__always_supported</span><span class="p">)</span></span><a href="#l60"></a>
<span id="l61"></span><a href="#l61"></a>
<span id="l62"><span class="n">__all__</span> <span class="o">=</span> <span class="n">__always_supported</span> <span class="o">+</span> <span class="p">(</span><span class="s1">&#39;new&#39;</span><span class="p">,</span> <span class="s1">&#39;algorithms_guaranteed&#39;</span><span class="p">,</span></span><a href="#l62"></a>
<span id="l63">                                <span class="s1">&#39;algorithms_available&#39;</span><span class="p">,</span> <span class="s1">&#39;pbkdf2_hmac&#39;</span><span class="p">)</span></span><a href="#l63"></a>
<span id="l64"></span><a href="#l64"></a>
<span id="l65"></span><a href="#l65"></a>
<span id="l66"><span class="n">__builtin_constructor_cache</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l66"></a>
<span id="l67"></span><a href="#l67"></a>
<span id="l68"><span class="k">def</span> <span class="nf">__get_builtin_constructor</span><span class="p">(</span><span class="n">name</span><span class="p">):</span></span><a href="#l68"></a>
<span id="l69">    <span class="n">cache</span> <span class="o">=</span> <span class="n">__builtin_constructor_cache</span></span><a href="#l69"></a>
<span id="l70">    <span class="n">constructor</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l70"></a>
<span id="l71">    <span class="k">if</span> <span class="n">constructor</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l71"></a>
<span id="l72">        <span class="k">return</span> <span class="n">constructor</span></span><a href="#l72"></a>
<span id="l73">    <span class="k">try</span><span class="p">:</span></span><a href="#l73"></a>
<span id="l74">        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s1">&#39;SHA1&#39;</span><span class="p">,</span> <span class="s1">&#39;sha1&#39;</span><span class="p">):</span></span><a href="#l74"></a>
<span id="l75">            <span class="kn">import</span> <span class="nn">_sha1</span></span><a href="#l75"></a>
<span id="l76">            <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;SHA1&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;sha1&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_sha1</span><span class="o">.</span><span class="n">sha1</span></span><a href="#l76"></a>
<span id="l77">        <span class="k">elif</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s1">&#39;MD5&#39;</span><span class="p">,</span> <span class="s1">&#39;md5&#39;</span><span class="p">):</span></span><a href="#l77"></a>
<span id="l78">            <span class="kn">import</span> <span class="nn">_md5</span></span><a href="#l78"></a>
<span id="l79">            <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;MD5&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;md5&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_md5</span><span class="o">.</span><span class="n">md5</span></span><a href="#l79"></a>
<span id="l80">        <span class="k">elif</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s1">&#39;SHA256&#39;</span><span class="p">,</span> <span class="s1">&#39;sha256&#39;</span><span class="p">,</span> <span class="s1">&#39;SHA224&#39;</span><span class="p">,</span> <span class="s1">&#39;sha224&#39;</span><span class="p">):</span></span><a href="#l80"></a>
<span id="l81">            <span class="kn">import</span> <span class="nn">_sha256</span></span><a href="#l81"></a>
<span id="l82">            <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;SHA224&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;sha224&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_sha256</span><span class="o">.</span><span class="n">sha224</span></span><a href="#l82"></a>
<span id="l83">            <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;SHA256&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;sha256&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_sha256</span><span class="o">.</span><span class="n">sha256</span></span><a href="#l83"></a>
<span id="l84">        <span class="k">elif</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s1">&#39;SHA512&#39;</span><span class="p">,</span> <span class="s1">&#39;sha512&#39;</span><span class="p">,</span> <span class="s1">&#39;SHA384&#39;</span><span class="p">,</span> <span class="s1">&#39;sha384&#39;</span><span class="p">):</span></span><a href="#l84"></a>
<span id="l85">            <span class="kn">import</span> <span class="nn">_sha512</span></span><a href="#l85"></a>
<span id="l86">            <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;SHA384&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;sha384&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_sha512</span><span class="o">.</span><span class="n">sha384</span></span><a href="#l86"></a>
<span id="l87">            <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;SHA512&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">cache</span><span class="p">[</span><span class="s1">&#39;sha512&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_sha512</span><span class="o">.</span><span class="n">sha512</span></span><a href="#l87"></a>
<span id="l88">    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l88"></a>
<span id="l89">        <span class="k">pass</span>  <span class="c1"># no extension module, this hash is unsupported.</span></span><a href="#l89"></a>
<span id="l90"></span><a href="#l90"></a>
<span id="l91">    <span class="n">constructor</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l91"></a>
<span id="l92">    <span class="k">if</span> <span class="n">constructor</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l92"></a>
<span id="l93">        <span class="k">return</span> <span class="n">constructor</span></span><a href="#l93"></a>
<span id="l94"></span><a href="#l94"></a>
<span id="l95">    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;unsupported hash type &#39;</span> <span class="o">+</span> <span class="n">name</span><span class="p">)</span></span><a href="#l95"></a>
<span id="l96"></span><a href="#l96"></a>
<span id="l97"></span><a href="#l97"></a>
<span id="l98"><span class="k">def</span> <span class="nf">__get_openssl_constructor</span><span class="p">(</span><span class="n">name</span><span class="p">):</span></span><a href="#l98"></a>
<span id="l99">    <span class="k">try</span><span class="p">:</span></span><a href="#l99"></a>
<span id="l100">        <span class="n">f</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">_hashlib</span><span class="p">,</span> <span class="s1">&#39;openssl_&#39;</span> <span class="o">+</span> <span class="n">name</span><span class="p">)</span></span><a href="#l100"></a>
<span id="l101">        <span class="c1"># Allow the C module to raise ValueError.  The function will be</span></span><a href="#l101"></a>
<span id="l102">        <span class="c1"># defined but the hash not actually available thanks to OpenSSL.</span></span><a href="#l102"></a>
<span id="l103">        <span class="n">f</span><span class="p">()</span></span><a href="#l103"></a>
<span id="l104">        <span class="c1"># Use the C function directly (very fast)</span></span><a href="#l104"></a>
<span id="l105">        <span class="k">return</span> <span class="n">f</span></span><a href="#l105"></a>
<span id="l106">    <span class="k">except</span> <span class="p">(</span><span class="ne">AttributeError</span><span class="p">,</span> <span class="ne">ValueError</span><span class="p">):</span></span><a href="#l106"></a>
<span id="l107">        <span class="k">return</span> <span class="n">__get_builtin_constructor</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l107"></a>
<span id="l108"></span><a href="#l108"></a>
<span id="l109"></span><a href="#l109"></a>
<span id="l110"><span class="k">def</span> <span class="nf">__py_new</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">):</span></span><a href="#l110"></a>
<span id="l111">    <span class="sd">&quot;&quot;&quot;new(name, data=b&#39;&#39;) - Return a new hashing object using the named algorithm;</span></span><a href="#l111"></a>
<span id="l112"><span class="sd">    optionally initialized with data (which must be bytes).</span></span><a href="#l112"></a>
<span id="l113"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l113"></a>
<span id="l114">    <span class="k">return</span> <span class="n">__get_builtin_constructor</span><span class="p">(</span><span class="n">name</span><span class="p">)(</span><span class="n">data</span><span class="p">)</span></span><a href="#l114"></a>
<span id="l115"></span><a href="#l115"></a>
<span id="l116"></span><a href="#l116"></a>
<span id="l117"><span class="k">def</span> <span class="nf">__hash_new</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">):</span></span><a href="#l117"></a>
<span id="l118">    <span class="sd">&quot;&quot;&quot;new(name, data=b&#39;&#39;) - Return a new hashing object using the named algorithm;</span></span><a href="#l118"></a>
<span id="l119"><span class="sd">    optionally initialized with data (which must be bytes).</span></span><a href="#l119"></a>
<span id="l120"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l120"></a>
<span id="l121">    <span class="k">try</span><span class="p">:</span></span><a href="#l121"></a>
<span id="l122">        <span class="k">return</span> <span class="n">_hashlib</span><span class="o">.</span><span class="n">new</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span></span><a href="#l122"></a>
<span id="l123">    <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></span><a href="#l123"></a>
<span id="l124">        <span class="c1"># If the _hashlib module (OpenSSL) doesn&#39;t support the named</span></span><a href="#l124"></a>
<span id="l125">        <span class="c1"># hash, try using our builtin implementations.</span></span><a href="#l125"></a>
<span id="l126">        <span class="c1"># This allows for SHA224/256 and SHA384/512 support even though</span></span><a href="#l126"></a>
<span id="l127">        <span class="c1"># the OpenSSL library prior to 0.9.8 doesn&#39;t provide them.</span></span><a href="#l127"></a>
<span id="l128">        <span class="k">return</span> <span class="n">__get_builtin_constructor</span><span class="p">(</span><span class="n">name</span><span class="p">)(</span><span class="n">data</span><span class="p">)</span></span><a href="#l128"></a>
<span id="l129"></span><a href="#l129"></a>
<span id="l130"></span><a href="#l130"></a>
<span id="l131"><span class="k">try</span><span class="p">:</span></span><a href="#l131"></a>
<span id="l132">    <span class="kn">import</span> <span class="nn">_hashlib</span></span><a href="#l132"></a>
<span id="l133">    <span class="n">new</span> <span class="o">=</span> <span class="n">__hash_new</span></span><a href="#l133"></a>
<span id="l134">    <span class="n">__get_hash</span> <span class="o">=</span> <span class="n">__get_openssl_constructor</span></span><a href="#l134"></a>
<span id="l135">    <span class="n">algorithms_available</span> <span class="o">=</span> <span class="n">algorithms_available</span><span class="o">.</span><span class="n">union</span><span class="p">(</span></span><a href="#l135"></a>
<span id="l136">            <span class="n">_hashlib</span><span class="o">.</span><span class="n">openssl_md_meth_names</span><span class="p">)</span></span><a href="#l136"></a>
<span id="l137"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l137"></a>
<span id="l138">    <span class="n">new</span> <span class="o">=</span> <span class="n">__py_new</span></span><a href="#l138"></a>
<span id="l139">    <span class="n">__get_hash</span> <span class="o">=</span> <span class="n">__get_builtin_constructor</span></span><a href="#l139"></a>
<span id="l140"></span><a href="#l140"></a>
<span id="l141"><span class="k">try</span><span class="p">:</span></span><a href="#l141"></a>
<span id="l142">    <span class="c1"># OpenSSL&#39;s PKCS5_PBKDF2_HMAC requires OpenSSL 1.0+ with HMAC and SHA</span></span><a href="#l142"></a>
<span id="l143">    <span class="kn">from</span> <span class="nn">_hashlib</span> <span class="kn">import</span> <span class="n">pbkdf2_hmac</span></span><a href="#l143"></a>
<span id="l144"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l144"></a>
<span id="l145">    <span class="n">_trans_5C</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">((</span><span class="n">x</span> <span class="o">^</span> <span class="mh">0x5C</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">256</span><span class="p">))</span></span><a href="#l145"></a>
<span id="l146">    <span class="n">_trans_36</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">((</span><span class="n">x</span> <span class="o">^</span> <span class="mh">0x36</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">256</span><span class="p">))</span></span><a href="#l146"></a>
<span id="l147"></span><a href="#l147"></a>
<span id="l148">    <span class="k">def</span> <span class="nf">pbkdf2_hmac</span><span class="p">(</span><span class="n">hash_name</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="n">salt</span><span class="p">,</span> <span class="n">iterations</span><span class="p">,</span> <span class="n">dklen</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l148"></a>
<span id="l149">        <span class="sd">&quot;&quot;&quot;Password based key derivation function 2 (PKCS #5 v2.0)</span></span><a href="#l149"></a>
<span id="l150"></span><a href="#l150"></a>
<span id="l151"><span class="sd">        This Python implementations based on the hmac module about as fast</span></span><a href="#l151"></a>
<span id="l152"><span class="sd">        as OpenSSL&#39;s PKCS5_PBKDF2_HMAC for short passwords and much faster</span></span><a href="#l152"></a>
<span id="l153"><span class="sd">        for long passwords.</span></span><a href="#l153"></a>
<span id="l154"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l154"></a>
<span id="l155">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">hash_name</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span></span><a href="#l155"></a>
<span id="l156">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="n">hash_name</span><span class="p">)</span></span><a href="#l156"></a>
<span id="l157"></span><a href="#l157"></a>
<span id="l158">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">password</span><span class="p">,</span> <span class="p">(</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">bytearray</span><span class="p">)):</span></span><a href="#l158"></a>
<span id="l159">            <span class="n">password</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">memoryview</span><span class="p">(</span><span class="n">password</span><span class="p">))</span></span><a href="#l159"></a>
<span id="l160">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">salt</span><span class="p">,</span> <span class="p">(</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">bytearray</span><span class="p">)):</span></span><a href="#l160"></a>
<span id="l161">            <span class="n">salt</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">memoryview</span><span class="p">(</span><span class="n">salt</span><span class="p">))</span></span><a href="#l161"></a>
<span id="l162"></span><a href="#l162"></a>
<span id="l163">        <span class="c1"># Fast inline HMAC implementation</span></span><a href="#l163"></a>
<span id="l164">        <span class="n">inner</span> <span class="o">=</span> <span class="n">new</span><span class="p">(</span><span class="n">hash_name</span><span class="p">)</span></span><a href="#l164"></a>
<span id="l165">        <span class="n">outer</span> <span class="o">=</span> <span class="n">new</span><span class="p">(</span><span class="n">hash_name</span><span class="p">)</span></span><a href="#l165"></a>
<span id="l166">        <span class="n">blocksize</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">inner</span><span class="p">,</span> <span class="s1">&#39;block_size&#39;</span><span class="p">,</span> <span class="mi">64</span><span class="p">)</span></span><a href="#l166"></a>
<span id="l167">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">password</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">blocksize</span><span class="p">:</span></span><a href="#l167"></a>
<span id="l168">            <span class="n">password</span> <span class="o">=</span> <span class="n">new</span><span class="p">(</span><span class="n">hash_name</span><span class="p">,</span> <span class="n">password</span><span class="p">)</span><span class="o">.</span><span class="n">digest</span><span class="p">()</span></span><a href="#l168"></a>
<span id="l169">        <span class="n">password</span> <span class="o">=</span> <span class="n">password</span> <span class="o">+</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\x00</span><span class="s1">&#39;</span> <span class="o">*</span> <span class="p">(</span><span class="n">blocksize</span> <span class="o">-</span> <span class="nb">len</span><span class="p">(</span><span class="n">password</span><span class="p">))</span></span><a href="#l169"></a>
<span id="l170">        <span class="n">inner</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">password</span><span class="o">.</span><span class="n">translate</span><span class="p">(</span><span class="n">_trans_36</span><span class="p">))</span></span><a href="#l170"></a>
<span id="l171">        <span class="n">outer</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">password</span><span class="o">.</span><span class="n">translate</span><span class="p">(</span><span class="n">_trans_5C</span><span class="p">))</span></span><a href="#l171"></a>
<span id="l172"></span><a href="#l172"></a>
<span id="l173">        <span class="k">def</span> <span class="nf">prf</span><span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="n">inner</span><span class="o">=</span><span class="n">inner</span><span class="p">,</span> <span class="n">outer</span><span class="o">=</span><span class="n">outer</span><span class="p">):</span></span><a href="#l173"></a>
<span id="l174">            <span class="c1"># PBKDF2_HMAC uses the password as key. We can re-use the same</span></span><a href="#l174"></a>
<span id="l175">            <span class="c1"># digest objects and just update copies to skip initialization.</span></span><a href="#l175"></a>
<span id="l176">            <span class="n">icpy</span> <span class="o">=</span> <span class="n">inner</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l176"></a>
<span id="l177">            <span class="n">ocpy</span> <span class="o">=</span> <span class="n">outer</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l177"></a>
<span id="l178">            <span class="n">icpy</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></span><a href="#l178"></a>
<span id="l179">            <span class="n">ocpy</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">icpy</span><span class="o">.</span><span class="n">digest</span><span class="p">())</span></span><a href="#l179"></a>
<span id="l180">            <span class="k">return</span> <span class="n">ocpy</span><span class="o">.</span><span class="n">digest</span><span class="p">()</span></span><a href="#l180"></a>
<span id="l181"></span><a href="#l181"></a>
<span id="l182">        <span class="k">if</span> <span class="n">iterations</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l182"></a>
<span id="l183">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">iterations</span><span class="p">)</span></span><a href="#l183"></a>
<span id="l184">        <span class="k">if</span> <span class="n">dklen</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l184"></a>
<span id="l185">            <span class="n">dklen</span> <span class="o">=</span> <span class="n">outer</span><span class="o">.</span><span class="n">digest_size</span></span><a href="#l185"></a>
<span id="l186">        <span class="k">if</span> <span class="n">dklen</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l186"></a>
<span id="l187">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">dklen</span><span class="p">)</span></span><a href="#l187"></a>
<span id="l188"></span><a href="#l188"></a>
<span id="l189">        <span class="n">dkey</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span></span><a href="#l189"></a>
<span id="l190">        <span class="n">loop</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l190"></a>
<span id="l191">        <span class="n">from_bytes</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span></span><a href="#l191"></a>
<span id="l192">        <span class="k">while</span> <span class="nb">len</span><span class="p">(</span><span class="n">dkey</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">dklen</span><span class="p">:</span></span><a href="#l192"></a>
<span id="l193">            <span class="n">prev</span> <span class="o">=</span> <span class="n">prf</span><span class="p">(</span><span class="n">salt</span> <span class="o">+</span> <span class="n">loop</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="s1">&#39;big&#39;</span><span class="p">))</span></span><a href="#l193"></a>
<span id="l194">            <span class="c1"># endianess doesn&#39;t matter here as long to / from use the same</span></span><a href="#l194"></a>
<span id="l195">            <span class="n">rkey</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">prev</span><span class="p">,</span> <span class="s1">&#39;big&#39;</span><span class="p">)</span></span><a href="#l195"></a>
<span id="l196">            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">iterations</span> <span class="o">-</span> <span class="mi">1</span><span class="p">):</span></span><a href="#l196"></a>
<span id="l197">                <span class="n">prev</span> <span class="o">=</span> <span class="n">prf</span><span class="p">(</span><span class="n">prev</span><span class="p">)</span></span><a href="#l197"></a>
<span id="l198">                <span class="c1"># rkey = rkey ^ prev</span></span><a href="#l198"></a>
<span id="l199">                <span class="n">rkey</span> <span class="o">^=</span> <span class="n">from_bytes</span><span class="p">(</span><span class="n">prev</span><span class="p">,</span> <span class="s1">&#39;big&#39;</span><span class="p">)</span></span><a href="#l199"></a>
<span id="l200">            <span class="n">loop</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l200"></a>
<span id="l201">            <span class="n">dkey</span> <span class="o">+=</span> <span class="n">rkey</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="n">inner</span><span class="o">.</span><span class="n">digest_size</span><span class="p">,</span> <span class="s1">&#39;big&#39;</span><span class="p">)</span></span><a href="#l201"></a>
<span id="l202"></span><a href="#l202"></a>
<span id="l203">        <span class="k">return</span> <span class="n">dkey</span><span class="p">[:</span><span class="n">dklen</span><span class="p">]</span></span><a href="#l203"></a>
<span id="l204"></span><a href="#l204"></a>
<span id="l205"></span><a href="#l205"></a>
<span id="l206"><span class="k">for</span> <span class="n">__func_name</span> <span class="ow">in</span> <span class="n">__always_supported</span><span class="p">:</span></span><a href="#l206"></a>
<span id="l207">    <span class="c1"># try them all, some may not work due to the OpenSSL</span></span><a href="#l207"></a>
<span id="l208">    <span class="c1"># version not supporting that algorithm.</span></span><a href="#l208"></a>
<span id="l209">    <span class="k">try</span><span class="p">:</span></span><a href="#l209"></a>
<span id="l210">        <span class="nb">globals</span><span class="p">()[</span><span class="n">__func_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">__get_hash</span><span class="p">(</span><span class="n">__func_name</span><span class="p">)</span></span><a href="#l210"></a>
<span id="l211">    <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></span><a href="#l211"></a>
<span id="l212">        <span class="kn">import</span> <span class="nn">logging</span></span><a href="#l212"></a>
<span id="l213">        <span class="n">logging</span><span class="o">.</span><span class="n">exception</span><span class="p">(</span><span class="s1">&#39;code for hash </span><span class="si">%s</span><span class="s1"> was not found.&#39;</span><span class="p">,</span> <span class="n">__func_name</span><span class="p">)</span></span><a href="#l213"></a>
<span id="l214"></span><a href="#l214"></a>
<span id="l215"><span class="c1"># Cleanup locals()</span></span><a href="#l215"></a>
<span id="l216"><span class="k">del</span> <span class="n">__always_supported</span><span class="p">,</span> <span class="n">__func_name</span><span class="p">,</span> <span class="n">__get_hash</span></span><a href="#l216"></a>
<span id="l217"><span class="k">del</span> <span class="n">__py_new</span><span class="p">,</span> <span class="n">__hash_new</span><span class="p">,</span> <span class="n">__get_openssl_constructor</span></span><a href="#l217"></a>
</pre>
</div>

<script type="text/javascript" src="/cpython/static/followlines.js"></script>

</div>
</div>



</body>
</html>

